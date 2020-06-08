# ipUtility

This tool is used to pool out information for given IPs and Masks.

I coded this for an exam to be able to get information without having to apply the network mask by hand for example.


Disclaimer !
-
There is no data verification, and the the code couldn't be more uggly. But I probably won't use it any time soon again, and it worked out fine for the 1h long exam.


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


