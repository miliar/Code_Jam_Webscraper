import sys
filename=sys.argv[1]
fi=open(filename,"r")
N=int(fi.readline())
TEXT="welcome to code jam"
L=len(TEXT)
for i in range(N):
  line=fi.readline()
  array=[1]+[0]*L
  for letter in line:
    for j in range(L):
      if TEXT[j]==letter:
        array[j+1]+=array[j]
  print "Case #%d: %04d"%(i+1,array[L]%10**4)

fi.close()
