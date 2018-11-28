import re
def f(a,size):
    pcake = []
    ans = 0
    for i in a:
        if(i=='-'):
            pcake.append(-1)
        else:
            pcake.append(+1)
    #for i in pcake:
    #    print i
    index = 0
    while index<len(pcake)-size+1:
        if(pcake[index]==-1):
            i = index
            ans+=1
            while(i<index+size):
                pcake[i]*=-1
                i+=1
        index+=1

    for i in pcake:
        if i==-1:
            return -1
    return ans

i = 0;
qfile = open("question.txt")
afile = open("answer.txt",'w+')
t = int(re.findall('\d+',qfile.readline())[0])
for i in range(1,t+1):
    line = qfile.readline()
    s = re.findall('[-+]{1}',line)
    k = int(re.findall('\d+',line)[0])
    ans = f(s,k)
    afile.write("Case #"+str(i)+": ")
    if ans==-1:
        afile.write("IMPOSSIBLE")
    else:
        afile.write(str(ans))
    afile.write("\n")
