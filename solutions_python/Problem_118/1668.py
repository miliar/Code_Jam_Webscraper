from C_small import isPalindrome
import time

def isDecent(n):
    d=0
    for i in range(len(str(n))):
        d+=int(str(n)[i])**2
        if d>9: return False
    return True

def readline_ints():
    return [int(num) for num in fin.readline().strip().split()]

# <codecell>

# Update this with the filename
fname = "C-large-1"
with open(fname+".in","r") as fin, open(fname+".out","w") as fout:
    numcases = readline_ints()[0]
    maxn=2001003
    decent=[num for num in range(1,maxn) if (isDecent(num) and isPalindrome(num))]
    for caseno in range(1, numcases+1):
        # Code goes here

        ran=readline_ints()
        a=ran[0]
        b=ran[1]
        result=0
        for i in range(len(decent)):
            if decent[i]**2>=a and decent[i]**2<=b: result+=1
            elif decent[i]**2>b: break
        outstr = "Case #%d: %s" % (caseno, result)
        fout.write(outstr + "\n")
