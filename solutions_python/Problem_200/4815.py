
f=open('B-small-attempt2.in.txt')
lines=f.readlines()
t =int(lines[0].strip())
print t
for j in xrange(1,t+1):

        n = int(lines[j].strip())
        # print n
        if(n == n%10):
                print "CASE #{0}: {1}".format(j, n)
                
        for i in reversed(xrange(11,n+1)):
                # print i
                num =i
                q =10
                r_prev=9999999999999999999
                flag =0
                while(i>0):
                        r = i%10;
                        i= i/10;
                        if(r_prev<r):
                                flag =-1

                        r_prev =r
                if(flag==0):
                        print "CASE #{0}: {1}".format(j, num)
                        break
        