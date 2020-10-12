#! python3
import os
import re


def exeCMD(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


# def writeFile(filename, data):
#     f = open(filename, "a")
#     f.write(data)
#     f.close

def getipv6():
    cmd = "ipconfig /all"
    text = exeCMD(cmd)
    part = re.compile("IPv6 地址[. ]+: ([a-z\d:]+)")
    ipaddr = re.findall(part, text)[0:2]
    return ipaddr


def getipv4():
    cmd = "ipconfig /all"
    text = exeCMD(cmd)
    part = re.compile("IPv4 地址[. ]+: ([.\d]+)")
    ipaddr = re.findall(part, text)
    return str(ipaddr)


if __name__ == "__main__":
    cmd = "ipconfig /all"
    result = exeCMD(cmd)
    IP = getipv6()
    IP4 = getipv4()
    print(IP)
    print(IP4)
