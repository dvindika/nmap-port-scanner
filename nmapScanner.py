import nmap

nmScan = nmap.PortScanner()

nmScan.scan('127.0.0.1', '1-10000')

print(nmScan.command_line())

for host in nmScan.all_hosts():
    print("--------------------------------")
    print("Host     : {0}  {1}".format(host, nmScan[host].hostname()))
    print("Status   : {0}".format(nmScan[host].state()))
    for protocol in nmScan[host].all_protocols():
        print("--------------------------------")
        print("Protocol : {0}".format(protocol))

        lport = nmScan[host][protocol].keys()

        for port in sorted(lport):
            print("port     : {0}     state     : {1}".format(port, nmScan[host][protocol][port]['state']))






