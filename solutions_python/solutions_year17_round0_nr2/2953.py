
fileName=str('C:\\Users\\Soheil\\Downloads\\B-large.in')
fin = open(fileName,'r')
fout = open('C:\\Users\\Soheil\\Documents\\outputtidylarge.txt', 'w')

t = int(fin.readline())  # read a line with a single integer
for i in range(1, t+1):
  a=list(fin.readline().rstrip())
  for j in range(len(a)-1,0,-1):
    if(int(a[j])<int(a[j-1])):
        if(int(a[j-1])>0):
            a[j-1]=str(int(a[j-1])-1)
            for k in range(j,len(a)):
                a[k]='9'
  if(int(a[len(a)-1])<1):
     a[0]='0';
     for l in range(1,len(a)):
        a[l]='9'
        break;
  fout.write("Case #{}: {}\n".format(i,int(''.join(a))))
fout.close()
fin.close()
#main.run()
