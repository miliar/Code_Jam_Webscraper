inp=open('D:\in.txt', 'rb')
output=open('D:\out.txt', 'w')
cases=int(inp.readline())
for case in range(0,cases):
    switches=0
    enginecount=int(inp.readline())
    if enginecount==0:
        s=('Case #'+str(case+1)+': 0\r\n')
        output.write(s)
        continue
    engines=[]
    for i in range(0,enginecount):
        engines.append(str(inp.readline()))
    
    querycount=int(inp.readline())
    if querycount==0:
        s=('Case #'+str(case+1)+': 0\r\n')
        output.write(s)
        continue
    queries=[]
    for i in range(0,querycount):
        queries.append(str(inp.readline()))
    position=0

    while queries!=[]:
        tempengines=[]
        for i in engines:
            if i in queries:
                tempengines.append(queries.index(i))
            else:
                tempengines.append(9999)
        tempengines.sort()
        tempengines.reverse()
        if (tempengines[0]==9999):
            break
        else:
            queries=queries[tempengines[0]:]
            switches=switches+1
    s=('Case #'+str(case+1)+': '+str(switches)+'\r\n')
    output.write(s)
output.write('\r\n')
output.close()
inp.close()

    

    
