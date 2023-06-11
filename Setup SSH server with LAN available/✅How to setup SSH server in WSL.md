Hi everyone. Today, I will show you how to setup SSH server in WSL which allow you to make SSH connection within your LAN. Use the link below to refer command being used in this video

To begin, we need to check whether there is another process occupy the port required by SSH server which is port 22 in powershell and terminal. To achieve this, use 
```bash
netstat -a
```
This command will show all TCP port which is being used. If your port is being used, you can stop that service which hold your port.

Next, install SSH server in WSL using 
```bash
sudo apt install openssh-server
```
Start `ssh` server
```bash
sudo service ssh start
sudo service ssh status
```
After you start your SSH server in WSL, you still need to configure to proxy SSH connection from window to WSL. This is because WSL had its own network which doesn't expose to LAN, you need to pass your SSH traffic from your window and window pass to WSL. To set proxy, you need to know what is your WSL IP address. After know WSL IP address, you will need replace your WSL IP address to this command to set proxy which route SSH traffic from window to WSL. Then you also need to specify what port you need to proxy from your window and to your WSL. For windows port, you can specify any port which isn't being used, but for WSL port, you need to specify port 22.
```powershell
# ref: https://learn.microsoft.com/en-us/windows/wsl/networking
# ref: https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-interface-portproxy
netsh interface portproxy add v4tov4 listenport=<windows port> listenaddress=0.0.0.0 connectport=<wsl port> connectaddress=<wsl ip address>
# eg:
# netsh interface portproxy add v4tov4 listenport=2222 listenaddress=0.0.0.0 connectport=22 connectaddress=192.168.101.100
```
For the command I used, it will proxy traffic from port 22 in windows to WSL port 22. You can specify any port number for windows port, but remember to make SSH connection to windows port you set here.

Next, you need to enable firewall from your window which allow inbound traffic from SSH to the port your specified
```powershell
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd) for WSL' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort <SSH port in window>
# eg
# New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd) for WSL' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

After you done above command, you can check using 
```bash
netstat -a
```
in window to check is that particular port is listening to the port you specified here. If yes, you can SSH toward your WSL SSH using windows' IP address.

Now, you are done with your SSH server, go to your client and install SSH client,
```bash
sudo apt install openssh-client
```

Then, connect to your SSH server using SSH command, remember to change the username to your Linux User
```bash
ssh <linux username>@<window server IP address> -p <your port set in netsh>
```
To get what is your window server IP address, use `ipconfig`

It will prompt you to enter your password if everything is OK. The password is your Linux's password

You probably will ask why is window IP address instead of WSL IP address. The reason we can do this because we had set our proxy using `netsh` command just now. 

If you want to uninstall your SSH server or SSH client, use below command,
```bash
sudo apt-get purge openssh-server
sudo apt-get purge openssh-client
```

Remember to remove the proxy if you want uninstall your SSH server
```powershell
netsh interface portproxy delete v4tov4 listenport= {Integer | ServiceName} [[listenaddress=] {IPv4Address | HostName} [[protocol=]tcp]
```

Show All proxy
```
netsh interface portproxy show v4tov4
```

In conclusion, to setup SSH server in WSL, you need to install openssh-server, enable the service, set the proxy to pass traffic from windows to WSL, and enable firewall to accept inbound SSH traffic to windows so that windows can pass the traffic to WSL. 

To SSH inside you SSH server, you need to used SSH command which include your windows' IP address, WSL user and the windows port you set in the proxy to WSL. 

That all for this video, you can leave comment below if you faced any problem. 