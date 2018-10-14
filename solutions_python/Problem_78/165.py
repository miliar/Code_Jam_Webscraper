import sys, fractions

#sys.stdin = open("in.txt")
sys.stdin = open("C:\\Users\\Kuldeep\\Downloads\\A-large.in")
sys.stdout = open("C:\\Users\\Kuldeep\\Desktop\\out.txt",'w')

t = int(raw_input())



for i in range(1,t+1):
    n, pd, pg = map(int,raw_input().split())
    a = pd
    b = 100
    while fractions.gcd(a,b)!=1 :
        c = fractions.gcd(a,b)
        a/=c
        b/=c
    if b>n:
        sys.stdout.write("Case #"+str(i)+": ")
        print "Broken"
    elif pd<100 and pg==100:
        sys.stdout.write("Case #"+str(i)+": ")
        print "Broken"
    elif pd>0 and pg==0:
        sys.stdout.write("Case #"+str(i)+": ")
        print "Broken"
    else:
        sys.stdout.write("Case #"+str(i)+": ")
        print "Possible"