def istidy(num):
    snum = str(num)
    l = len(snum)
    for i in range(l-1):
        if snum[i]>snum[i+1]:
            return False,int(snum[i]),int(snum[i+1])
    return True,0,0

def tidyNumbers(num):
    cond,lnum,rnum = istidy(num)
    while not cond :
        #print num,lnum,rnum
        if lnum==1 and rnum==0:
            newlen=len(str(num))-1
            num=10**newlen-1
            #print num
        else:
            num-=1
        cond,lnum,rnum = istidy(num)
    return num

inputfname ="B-small-attempt0.in" #"A-small-practice.in"
outputfname = inputfname+".out"
with open(inputfname,"r") as f:
    lines = f.readlines()
lines2 = [
'4',
'132',
'1000',
'7',
'111111111111111110' ,      
]
n = int(lines[0].strip('\n'))
with open(outputfname,"w") as f:
     f.write('')
with open(outputfname,"a") as f:
    for i in range(1,n+1):
        num = long (lines[i].strip('\n'))
        #print '----',num
        outstring = 'Case #'+str(i)+': '+str(tidyNumbers(num))
        print outstring
        f.write(outstring+"\n")