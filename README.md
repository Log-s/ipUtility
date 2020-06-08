# ipUtility

This tool is used to pool out information for given IPs and Masks.

I coded this for an exam to be able to get information without having to apply the network mask by hand for example.


Disclaimer !
-
There is no data verification, and the the code couldn't be more **uggly**. But I probably won't use it any time soon again, and it worked out fine for the hour long exam.


Features :
-
The tool can print out : 
*the ip's class
*the ip corresponding binary value*
*the masks corresponding binary value
*the network part of the ip
*the local part of the ip
*the network's broadcasting adress
*the subnet the machine is on
*the subnet's broadcasting adress
*the number of possible subnets for the given ip/mask couple
*the amount of possible machines per subnet


Install & Run
-
Python3 should be installed on the computer.

Run :

```python3 ipUtility.py```


Use
-
commands :

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


