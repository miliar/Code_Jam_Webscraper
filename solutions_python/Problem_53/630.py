f_name = 'large'
fin = open(f_name + '.in',"r")
fout = open(f_name + '.out',"w")
c = 0
line = fin.readline()
n=0;k=0;a=0;b=0
x=int(line)
while x>0:
    line = fin.readline()
    n,k = [int(i) for i in line.split()]
    a = 2**n
    b = k-(a-1)
    if b%a == 0 and n !=0:
        fout.write("Case #" + str(c+1) + ": ON\n")
    else:
        fout.write("Case #" + str(c+1) + ": OFF\n")
    c+=1
    x-=1
fin.close()
fout.close()
