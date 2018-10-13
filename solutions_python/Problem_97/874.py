import sys
filename=sys.argv[1]
infile=open(filename,"r")
outfile=open("google.out","w")
count=0
list=[]
line=''
for line in infile:
    if count==0:
        count+=1
        continue
    else:

        count+=1
        list=line.split()
        N=int(list.pop(0))
        S=int(list.pop(0))
        p=int(list.pop(0))
        S_helps=0
        num=0
        out=0
        while N!=0:
            N=N-1
            num=int(list.pop(0))
            #print str(num//3)+" "+str(num%3)+" p "+str(p)
            if num==0 and p>0:
                S_helps+=1
            elif num==0 and p==0:
                out+=1
            elif ((num//3)>=p and (num%3)==0) or (((num//3)+1)>=p and (num%3)==1) or (((num//3)+1)>=p and (num%3)==2):
                out+=1
                #print "out increases"
            elif S>0 and (((num//3+1)>=p and (num%3)==0) or  (((num//3)+2)>=p and (num%3)==2)):
                out+=1
                #print "out increases"+" S"+str(S)
                S-=1
        outfile.write( "Case #"+str(count-1)+": "+str(out)+"\n")
print "Done"
outfile.close()






