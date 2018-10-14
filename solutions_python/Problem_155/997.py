f = open('C:/Users/rajiv/Desktop/code jam 15/A-large.out', 'w')
lines = [line.strip() for line in open('C:/Users/rajiv/Desktop/code jam 15/A-large.in')]
result=0
for i in range(1, int(lines[0]) + 1):
    j = lines[i].split()
    p = list(j[1])

    m=int(p[0])
    for c in range(1,p.__len__()):
        if m<c and p[c]>0:
            result=result+c-m
            m=c
        m+=int(p[c])
        #print 'p['+c.__str__()+'] :'+p[c]+'  m='+m.__str__()
    print 'Case #'+i.__str__()+': '+ result.__str__()#+'  '+m.__str__()
    f.write('Case #'+i.__str__()+': '+ result.__str__()+'\n')
    result=0

f.close()