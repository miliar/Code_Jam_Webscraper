infile=open('B-large.in','r')
outfile=open('B-large-output.in','a')

first=True
l=0
for line in infile:
    impossible=False
    l=l+1
    if first==True:
        first=False
        continue
    line=line.split(" ")
    untidy=list(line[0])
    for t in range(len(untidy)-1):
        change=False
        for i in range(len(untidy)-1):
            if len(untidy)==2:
                break
            if change==True:
                untidy[i]=str(9)
                continue
            if untidy[i+1]=='\n':
                break
            if int(untidy[i])>int(untidy[i+1]):
                untidy[i]=str(int(untidy[i])-1)
                untidy[i+1]='9'
                change=True
                continue

    outfile.write('Case #'+str(l-1)+': '+str(int(''.join(untidy)))+'\n')
