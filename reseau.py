"""

Gives information about a network, using IP adresses and masks

ip@ : specefies an IP
ma@  : specefies a mask
cl@  : specefies class (works with mask only)
&   : operator to bind to options
q   : exists the program

combinations :
    ip@
    ip@&/xx (xx : number of 1 values in mask adress)
    ip@&m@
    ma@
    ma@&c@
    cl@

example :
    ip@127.0.0.1&m@255.255.255.0
    ip@127.0.0.1&/22
    m@255.255.255.0&c@B

"""

print ("Welcome !\n\nGives information about a network, using IP adresses and masks\n\nip@ : specefies an IP\nma@  : specefies a mask\ncl@  : specefies class (works with mask only)\n&   : operator to bind to options\nq   : exists the program\n\ncombinations :\n\tip@\n\tip@/xx (xx : number of 1 values in mask adress)\n\tip@&ma@\n\tma@\n\tma@&cl@\n\tcl@\n\nexample : \n\tip@127.0.0.1&ma@255.255.255.0\n\tip@127.0.0.1/22\n\tma@255.255.255.0&cl@B\n\tcl@A\n")
inData = ""
composed = False
ip = "/"
bIp = "/"
mask = "/"
bMask = "/"
netId = "/"
localId = "/"
classe = "/"
broadcast = "/"
subnet = "/"
subBroadcast = "/"
nbSubnet = "/"
nbMachine = "/"

def printInfos():
    print  ("\nIP :\t"+ip+"\t\t\t\tclasse :\t"+classe+"\n"
            "Mask :\t"+mask+"\t\t\t\tNetID :\t\t"+netId+"\n"
            "bIP :\t"+bIp+"\tMachine ID :\t"+localId+"\n"
            "BMask :\t"+bMask+"\tBroadcast :\t"+broadcast+"\n"
            "\n"
            "Subnet : "+subnet+"\t\t\t\tSubnet Broadcast : "+subBroadcast+"\n"
            "\n"
            "Number of possible subnets :\t\t"+nbSubnet+"\n"
            "Number of possible machines(/subnet):\t"+nbMachine+"\n\n")

def reset():
    global composed,classe,ip,bIp,mask,bMask,netId,localId,broadcast,subnet,subBroadcast,nbSubnet,nbMachine
    ip = ""
    bIp = ""
    mask = ""
    bMask = ""
    netId = ""
    localId = ""
    classe = ""
    broadcast = ""
    subnet = ""
    subBroadcast = ""
    nbSubnet = ""
    nbMachine = ""
    composed = False

def calculate():
    global classe,ip,bIp,mask,bMask,netId,localId,broadcast,subnet,subBroadcast,nbSubnet,nbMachine
    if mask != "":
        m = mask.split(".")
        for i in m:
            tmp = str("{0:b}".format(int(i)))
            if len(tmp) < 8:
                tmp = "0"*(8-len(tmp))+tmp
            bMask += tmp+" "
    elif bMask != "":
        bMask = bMask[:8] + " " + bMask[8:16] + " " + bMask[16:24] + " " + bMask[24:32]
        m = bMask.split(" ")
        for i in m:
            mask += str(int(i,2)) + "."
        mask = mask[:-1]
    if ip != "":
        m = ip.split(".")
        for i in m:
            tmp = str("{0:b}".format(int(i)))
            if len(tmp) < 8:
                tmp = "0"*(8-len(tmp))+tmp
            bIp += tmp+" "
    if classe == "" and ip != "":
        m = ip.split(".")
        if int(ip.split(".")[0]) < 128:
            classe = "A"
            netId = m[0]+".0.0.0"
            broadcast = m[0]+".255.255.255"
            localId = "0."+m[1]+"."+m[2]+"."+m[3]
        elif int(m[0]) < 192:
            classe = "B"
            netId = m[0]+"."+m[1]+".0.0"
            broadcast = m[0]+"."+m[1]+".255.255"
            localId = "0.0."+m[2]+"."+m[3]
        elif int(m[0]) < 224:
            classe = "C"
            netId = m[0]+"."+m[1]+"."+m[2]+".0"
            broadcast = m[0]+"."+m[1]+"."+m[2]+".255"
            localId = "0.0.0."+m[3]
        elif int(m[0]) < 240:
            classe = "D"
        else:
            classe = "E"
    if bMask != "" and classe != "":
        if classe == "A":
            n = 0
            for i in range(8,32):
                if (bMask.replace(" ","")[i]) == "0":
                    break
                n += 1
        if classe == "B":
            n = 0
            for i in range(16,32):
                if (bMask.replace(" ","")[i]) == "0":
                    break
                n += 1
        if classe == "C":
            n = 0
            for i in range(24,32):
                if (bMask.replace(" ","")[i]) == "0":
                    break
                n += 1
        nbSubnet = str(2**n)
        if nbSubnet == "1":
            nbSubnet = "0"
    if bIp != "" and bMask != "":
        subnet = '{0:b}'.format(int(bIp.replace(" ",""),2) & int(bMask.replace(" ",""),2))
        while len(subnet) < 32:
            subnet = '0'+subnet
        subnet = subnet[:8] + " " + subnet[8:16] + " " + subnet[16:24] + " " + subnet[24:]
        m = subnet.split()
        subnet = ""
        for i in m:
            tmp = str(int(i,2))
            subnet += tmp+"."
        subnet = subnet[:-1]
    if subnet != "" and bMask != "":
        m = subnet.split(".")
        s = ""
        for j in m:
            tmp = str("{0:b}".format(int(j)))
            if len(tmp) < 8:
                tmp = "0"*(8-len(tmp))+tmp
            s += tmp
        i = 0
        while i<32 and bMask.replace(" ","")[i] == "1":
            i +=1
        subBroadcast = s[:i] + "1"*(32-i)
        subBroadcast = subBroadcast[:8] + " " + subBroadcast[8:16] + " " + subBroadcast[16:24] + " " + subBroadcast[24:32]
        m = subBroadcast.split()
        subBroadcast = ""
        for i in m:
            subBroadcast += str(int(i,2))+"."
        subBroadcast = subBroadcast[:-1]
    if bMask != "":
        i=0
        while i<32 and bMask.replace(" ","")[i] == "1":
            i +=1
        nbMachine = str((2**(32-i))-2)
    if ip == "":
        ip = "/\t"
    if mask == "":
        mask = "/\t"
    if bIp == "":
        bIp = "/\t\t\t\t"
    if bMask == "":
        bMask = "/\t\t\t\t"
    if classe == "":
        classe = "/"
    if netId == "":
        netId = "/"
    if localId == "":
        localId = "/"
    if broadcast == "":
        broadcast = "/"
    if subBroadcast == "":
        subBroadcast = "/"
    if subnet == "":
        subnet = "/\t"
    if nbSubnet == "":
        nbSubnet = "/"
    if nbMachine == "":
        nbMachine = "/"
    printInfos()

while True:

    reset()

    inData = input("> ")

    if inData == "q" or inData == "Q":
        print("Exiting...")
        break

    c1 = inData[:3]
    if "&" in inData:
        composed = True

    if c1 == "ip@":
        if not composed:
            ip = inData[3:]
        else:
            ip = inData[3:inData.index("&")]
            if inData[inData.index("&")+1:inData.index("&")+4] == "ma@":
                mask = inData[inData.index("&")+4:]
            elif inData[inData.index("&")+1] == "/":
                bMask = ""
                try:
                    x = int(inData[inData.index("&")+2:])
                except:
                    print ("Invalid Format /xx : x must be integers")
                    continue
                for i in range (x):
                    bMask += "1"
                if len(bMask) < 32:
                    bMask += "0"*(32-len(bMask))
                elif (lenbMask) > 32:
                    print ("Invalid value /xx : xx maximum value is 32")
        calculate()

    elif c1 == "ma@":
        if not composed:
            mask = inData[3:]
        else:
            mask = inData[3:inData.index("&")]
            classe = inData[inData.index("&")+4]
        calculate()

    elif c1 == "cl@":
        classe = inData[3]
        if classe == "A":
            print("Range : 0.0.0.0 - 127.255.255.255\n")
        elif classe == "B":
            print("Range : 128.0.0.0 - 191.255.255.255\n")
        elif classe == "C":
            print("Range : 192.0.0.0 - 223.255.255.255\n")
        elif classe == "D":
            print("Range : 224.0.0.0 - 239.255.255.255\n")
        else:
            print("Range : 240.0.0.0 - 247.255.255.255\n")

    else:
        print("Unexpected symbol : {}".format(c1))
        continue
