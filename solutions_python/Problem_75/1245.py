f=open("B-small-attempt1.in",'r')
w=open("output.out",'w')
trials=int(f.readline())
position=0;
combinelist=''
opposed=''
for x in range(1,trials+1):
    position=0
    thestuff=f.readline().split()
    numcombine=thestuff[position]
    position+=1
    if numcombine!='0':
        combinelist=thestuff[position]
        position+=1
    numopposed=thestuff[position]
    position+=1
    if numopposed!='0':
        opposed=thestuff[position]
        position+=1
    numelements=thestuff[position]
    position+=1
    elementliststring=thestuff[position]
    elementlist=[]
    elementlist.append(elementliststring[0])
    y=1
    z=1
    while z<len(elementliststring):
        elementlist.append(elementliststring[z])
        if len(combinelist)!=0:
            if (elementlist[y-1]==combinelist[0] and elementlist[y]==combinelist[1]) or (elementlist[y-1]==combinelist[1] and elementlist[y]==combinelist[0]):
                elementlist.pop(y)
                elementlist.pop(y-1)
                y-=1
                elementlist.append(combinelist[2])
        if len(opposed)!=0:
            if elementlist.count(opposed[0])!=0 and elementlist.count(opposed[1])!=0:
                del elementlist[:]
                z+=1
                if(z<=len(elementliststring)-1):
                    elementlist.append(elementliststring[z])
                y=0
        z+=1
        y+=1
    output='Case #' + str(x) + ': ['
    for x in range(0,len(elementlist)):
        if x == len(elementlist)-1:
            output+=str(elementlist[x])
        else:
            output+=str(elementlist[x]) + ', '
    output+=']\n'
    w.write(output)
f.close()
w.close()
