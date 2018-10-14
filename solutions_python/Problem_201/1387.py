
import sys
import math

out=open("out.txt","w")
with open("input.txt","r") as f:
    n=int(f.readline().strip())
    for j in range(n):
        n,k=map(int,f.readline().strip().split(' '))
        print n,k

        if(k>n/2 and False):
            out.write("Case #%d: %d %d\n" %(j+1,0,0))
        elif(k==1 and False):
            out.write("Case #%d: %d %d\n" % (j + 1, int(n / 2), int((n-1) / 2)))
        else:
            level = math.floor(math.log(k,2))

            user_on_level = math.pow(2, level)
            #print "level=%d   users_on_level=%d" % (level, user_on_level)
            a=0
            b=(n-user_on_level+1)%user_on_level
            #print "b=%d" % b
            if(k-user_on_level+1>b):
                a = int(math.floor((n - user_on_level + 1) / user_on_level))
            else:
                a=int(math.ceil((n - user_on_level + 1) / user_on_level))
            out.write("Case #%d: %d %d\n" % (j + 1, int(a / 2), int((a-1) / 2)))
        #print '\n\n'