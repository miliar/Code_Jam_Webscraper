import math

def demo():
    a=open("C-large-1.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        line = b[i+1][:-1].split(" ")
        
        res=check(line)
                
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

A=0L
B=0L

def check(case):
    global A
    global B
    global fas
    A=long(case[0])
    B=long(case[1])
    return len(filter(between, fas))

def between(x):
    global A 
    global B 
    return A <= x and x <= B

def generateFAS(exp_max):
    return filter(isPalindrome, [long(i)**2 for i in filter(isPalindrome, xrange(1+10**(exp_max/2)))])

def isPalindrome(n):
    sn=list(str(n))
    sr=sn[:]
    sr.reverse()
    return sn==sr

expo = raw_input("Max exp (even only!):")
fas = generateFAS(int(expo))
print fas
raw_input("Got data?")
demo()
