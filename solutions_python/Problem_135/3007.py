__author__ = 'Musunurus'

file=open("A-small-attempt1.in",'r')
file2=open("output.txt",'w')
t=int(file.readline())
d=[]
for i in range(2*t):

    d.append(int(file.readline()))
    k=[file.readline().split() for i in range(4)]
    for p in range(4):
        for q in range(4):
            k[p][q]=int(k[p][q])
    d.append(k)
    n=1
file.close()
for i in [k for k in range(4*t) if(k%4==0)]:

    l1=d[i+1][d[i]-1]
    l2=d[i+3][d[i+2]-1]
    elem=None
    count=0
    for i in l1:
        if i in l2:
            elem=i
            count+=1
    if(count==1):
        file2.write("Case #"+str(n)+": "+str(elem)+"\n")
    elif count>1:
        file2.write("Case #"+str(n)+": Bad magician!\n")
    else:
        file2.write("Case #"+str(n)+": Volunteer cheated!\n")

    n+=1


file2.close()
