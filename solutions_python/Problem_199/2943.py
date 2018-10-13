infile=open('A-large.in.txt','r')
outfile=open('A-large-output.txt','a')

first=True
l=0
for line in infile:
    impossible=False
    l=l+1
    if first==True:
        first=False
        continue
    line=line.split(" ")
    pancakes=list(line[0])
    K=int(line[1])
    flips=0

    for i in range(len(pancakes)):
        if pancakes[i]=='-':
            for j in range(K):
                if (i+j)>(len(pancakes)-1):
                    impossible=True
                    continue
                pancakes[i+j]='+' if pancakes[i+j]=='-' else '-'
            flips=flips+1
    if impossible==True:
        outfile.write('Case #'+str(l-1)+': '+'IMPOSSIBLE\n')
    else:
        outfile.write('Case #'+str(l-1)+': '+str(flips)+'\n')
