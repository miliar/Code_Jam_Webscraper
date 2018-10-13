from math import sqrt,ceil,floor

def is_pal(x):
    s=str(x)
    l=len(s)
    if l%2==0:
        if s[0:l/2]==s[l:l/2-1:-1]:
            return True
        else:
            return False
    else:
        if s[0:(l-1)/2]==s[l:(l-1)/2:-1]:
            return True
        else:
            return False

def generate():
#big fair is 2001002 in range 1,10000000
    for x in range(1,2001003):
        if is_pal(x) and is_pal(x**2):
            fair.append(x)
    print "Gen Done!"

def solve(fl):
    l=fl.split()
    c=0
    a=int(ceil(sqrt(int(l[0]))))
    b=int(floor(sqrt(int(l[1]))))
    for x in fair:
        if x>=a and x<=b:
            c+=1
    return str(c)

fair=[]
generate()

fi = open("C-large-1.in","r")
fo = open("C-large-1.out","w")

n = int(fi.readline())

for i in range(1,n+1):
    fl = fi.readline()
    o= "Case #"+str(i)+": "+solve(fl)
#    print o
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
