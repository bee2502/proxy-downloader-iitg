import os
import urllib2

def downloader(url,fname,proxy="",increment=200) :
    data = urllib2.urlopen(url)
    size= data.headers["Content-Length"]
    start = 0
    increment = increment*1024*1024 #default 200 MB increments
    part = 1
    curr = start
    while (start < size):
    	cmd = "curl -x " + str(proxy) + " -o ubuntu.iso." + str(part) + " -r" + str(start) + "-" + str(curr) + " -L " + str(url) + " & "
    	os.system(str(cmd))	
    	start = curr 
    	curr = curr + inc
    	part = part + 1
    cmd = "cat "+str(fname)+".* > "+str(fname)

url = "https://download.fedoraproject.org/pub/fedora/linux/releases/23/"+/
      "Workstation/x86_64/iso/Fedora-Live-Workstation-x86_64-23-10.iso"
fname = "fedora.iso"
proxy = "http://d.harsh:9Harsh@202.141.80.20:3128"
downloader(url,fname,proxy)    
