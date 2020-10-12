Installation guide (ubuntu), write the following commands in the terminal:
1.	echo "deb [trusted=yes] https://apt.fury.io/caddy/ /" \
    | sudo tee -a /etc/apt/sources.list.d/caddy-fury.list
2.	sudo apt update
3.	sudo apt install caddy

*Taken from: https://caddyserver.com/docs/download

How to use:

*to run in http/1.1 without encryption open the terminal in the folder containing the index.html and use the command: sudo caddy file-server
*to run http/1.1 with encryption use the same steps as HTTP/2 shown below and block HTTP/2 in the browser

to run http/2 or http/3 follow these steps:

create an empty document called "Caddyfile" (upper-case 'C')

* to use in the public network you must assign a domain to get a certificate, use a free DNS to get one

write the following in the Caddyfile to use HTTP/2:

your.domain { 
	tls your.email # (can be replaced with "internal" to use it locally but can only be reached #using curl, browsers would raise an error)
   	file_server
}

to use HTTP/3 add the following above everything else in the Caddyfile:

{

	experimental_http3
	
}

after editing the Caddyfile open the terminal in the folder containing the index.html file and the Caddyfile document you created and use the command: sudo caddy run --watch
* stop the server by using sudo caddy stop
* make sure to open the ports you wish to use in your router, you can use other ports but the browsers won't recognize them automatically.
* make sure to open the ports in the operating system firewall.
* http/1.1 without encryption uses port 80 (TCP)
* http/2 and http/3 (uses https) use the port 443, http/2 uses TCP, http/3 uses Quic (UDP).
