square=[1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L]

'''def issquare(n):
    
    h = n & 0xF
    if h > 9:
        return [False,-1]
    if h!=2 and h!=3 and h!=5 and h!=6 and h!=7 and h!=8:
        t=int(n**0.5)
        return [int(t+0.5)**2==n,t]
    return [False,-1]
'''

'''def ispal(n):
    string=str(n)
    if string==string[::-1]:
        return True
    else:
        return False
'''
#source="C:\Users\Mani\Desktop\C-small-attempt0.in"
source="C:\Users\Mani\Desktop\C-large-1.in"
dest="C:\Users\Mani\Desktop\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
t=int(t)
for i in range(t):
    m=fin.readline()
    m=m.split(" ")
    m=map(int,m)
    n=m[0]
    s=m[1]
    c=0
    j=n
    con=[ii for ii in square if ii>=n and ii<=s]
    c=len(con)
    c=str(c)
    i=str(i+1)
    fout.write("Case #"+i+": "+c+"\n")
fin.close()
fout.close()
