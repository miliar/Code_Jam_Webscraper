def main():
    global people
    f=open("A-large.in",'r')
    lines=[]
    for line in f:
        lines.append(line.split())
    f.close()
    cases=lines.pop(0)
    maxshy=0
    allshy=0
    out=''
    for case in range(int(cases[0])):
        maxshy=lines[case][0]
        allshy=list(lines[case][1])
        for i in range(len(allshy)):
            allshy[i]=int(allshy[i])
        people=0
        pneeded(maxshy,allshy)
        if case==(int(cases[0])-1):
            out+='Case #'+str(case+1)+': '+str(people)
            break
        out+='Case #'+str(case+1)+': '+str(people)+'\n'
        people=0
    of=open("output.txt","w")
    of.write(out)
    
            
            
def pneeded(maxshy,allshy):
    global people
    if maxshy==0:
        return
    clapping=0
    for i in range(len(allshy)):
        if int(allshy[i])==0:
            continue
        if i>clapping:
            people+=i-clapping
            clapping+=i-clapping
        clapping+=allshy[i]

    
main()