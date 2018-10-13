'''
Created on Apr 13, 2013

@author: camgelo
'''
import sys

dicMap = {'X':1,'O':-1,'.':100,'T':0}

def handle(count, lines):
    matrix=[]
    d1=0
    d2=0
    col=[0,0,0,0]
    sum=0
    for num,line in enumerate(lines):
        n = reduce(lambda x,y:x+y, [dicMap[c] for c in line])
        if 5>n>=3:
            return 'X won'
        if n<=-3:
            return 'O won'
        for i,c in enumerate(line):
            col[i]+=dicMap[c]
        d1+=dicMap[line[num]]
        d2+=dicMap[line[3-num]]
        sum+=n
    for n in col:
        if 5>n>=3:
            return 'X won'
        if n<=-3:
            return 'O won' 
    if 5>d1>=3 or 5>d2>=3:
        return 'X won'
    if d1<=-3 or d2<=-3:
        return 'O won'
    n = reduce(lambda x,y:x+y, col)
    assert(n==sum)
    if n>16:
        return 'Game has not completed'

    return 'Draw'
    
def main():
    input = sys.argv[1]
    f=file(input)
    num = int(f.readline().strip())
    count=1
    lines=[]
    output=file('output.txt','wb')
    for line in f:
        line=line.strip()
        if line:
            print line
            lines.append(line)
        if len(lines)==4:
            result = handle(count, lines)
            print "Case #%s: %s"%(count,result)
            print 
            output.write("Case #%s: %s\r\n"%(count,result))
            count+=1
            lines=[]

if __name__=='__main__':
    main() 