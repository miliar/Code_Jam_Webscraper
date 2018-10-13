def test(num):
    while num%2==0:
        num/=2
    if num==1:
        return True
    return False


infile = open('A-small-attempt0 (1).in','r')
t = int(infile.readline())
outfile = open('a-out.txt','w')
for i in range(t):
    a,b = infile.readline().split('/')
    a=int(a)
    b=int(b)
    while a%2==0 and b%2==0:
        a/=2
        b/=2
    outfile.write('Case #'+str(i+1)+': ')
    if test(b):    
        s=0
        while a<b:
            s+=1
            a*=2    
        outfile.write(str(s)+'\n')
    else:
        outfile.write('impossible\n')

outfile.close()
infile.close()
