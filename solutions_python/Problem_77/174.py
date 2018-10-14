__author__ = 'lex'
input=open("int","r")
out=open("out","w")
n=int(input.readline())

def calc(count):
    if count==0:return 0
    if count==2:return 2
    if count==3:return 4
    if count==4:return 4
    if count==5:return 6
    return 2+(count-1)
for s in xrange(n):
    m=int(input.readline())
    line = input.readline()
    line=line[:-1]
    line=line.split(' ')
    line=[int(x) for x in line]

    prob=0

    sort_line=line[:]
    sort_line.sort()
    count=0
    for i in range(len(line)):
        if line[i]!=sort_line[i]:
            count+=1
    '''count1=0
    for i in range(len(line)):
        if line[i]!=sort_line[i] and line[line[i]-1]==(i+1):
            count1+=1
    prob=count1*2
    count-=count1
    prob+=calc(count)'''
    out.write('Case #%s: %.6f\n' %((s+1).__str__(),count))

  