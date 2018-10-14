file=open("A-small-attempt1.in")
outfile=open("Asmall1output.ou", "w")
N=int(file.readline())
for i in range (N):
    a=int(file.readline())
    D1=[set(int(num) for num in file.readline().split(' ')) for item in range(4)]
    b=int(file.readline())
    D2=[set(int(num) for num in file.readline().split(' ')) for item in range(4)]
    c=D1[a-1].intersection(D2[b-1])
    print()
    if (len(c)>1):
        outfile.write("Case #"+str(i+1)+": Bad magician!\n")
    elif (len(c)<1):
        outfile.write("Case #"+str(i+1)+": Volunteer cheated!\n")
    else:
        outfile.write("Case #"+str(i+1)+": "+str(c.pop())+"\n")
