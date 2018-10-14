__author__ = 'Tuhin Kundu'
with open("B-small-attempt1.in","r") as input,open("sampout.txt","w") as output:
    t=int(input.readline())
    for i in xrange(1,t+1):
        n=int(input.readline())
        while(n>=0):
            tmp=int("".join(sorted(list(str(n)))))
            if n==tmp:
                output.write("Case #"+str(i)+": "+str(tmp)+"\n")
                break
            n-=1


