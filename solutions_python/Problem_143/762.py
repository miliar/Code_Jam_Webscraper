import sys
input_from_file=True
fout=open("G:/o.txt","w")
if input_from_file:
    f=open("G:/ab.txt","r")
else:
    f=sys.stdin
t=int(f.readline())
for i in range(t):
   s=f.readline()
   c=0
   A,B,N=map(int,s.split())
   for j in range(A):
    for k in range(B):
        p=j&k
        if(p<N):
            c=c+1
   output="Case #" + str(i+1) + ": " + str(c) + "\n"
   fout.write(output)
fout.close()
f.close()



print "done"
