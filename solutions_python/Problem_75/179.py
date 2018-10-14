__author__ = 'lex'
input=open("int","r")
out=open("out","w")
n=int(input.readline())

def modify(str="",invoke={},opposed=[]):
    new_str=str
    for key,rep in invoke.iteritems():
        new_str=new_str.replace(key,rep)
    for elem in opposed:
        if (elem[0] in new_str) and (elem[1] in new_str):
            new_str=""
            break
    return new_str
    
for s in xrange(n):
    line = input.readline()
    line=line[:-1]
    line=line.split(' ')
    invoke={}
    opposed=[]
    C=int(line[0])
    for i in range(1,C+1):
        invoke[''.join((line[i][0],line[i][1]))]=line[i][2]
        invoke[''.join((line[i][1],line[i][0]))]=line[i][2]

    D=int(line[C+1])
    
    for i in range(C+2,C+2+D):
        opposed.append((line[i][1],line[i][0]))
        opposed.append((line[i][0],line[i][1]))

    str=line[-1]
    new_str=""
    for i in str:
        new_str+=i
        new_str=modify(new_str,invoke,opposed)
        
    if len(new_str):
        out.write('Case #%s: [' %((s+1).__str__()))
        for i in new_str[:-1]:
            out.write("%s, "%(i.__str__()))
        out.write('%s]\n' %((new_str[-1]).__str__()))
    else:
        out.write('Case #%s: []\n' %((s+1).__str__()))

  