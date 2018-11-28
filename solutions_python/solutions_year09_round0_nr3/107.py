'''
Created on 2009-9-3

@author: ufo
'''
import re
from collections import defaultdict
def countpattern(text,l,index):
    global sequence,d
    if l==len(sequence):
        return 1
    count=0
    tempcount=0
    upbound=len(text)-len(sequence)+l+1
    if index<upbound:
        for i in range(index,upbound):
            if text[i]==sequence[l]:
                if d.has_key((l,i)):
                    count+=d.get((l,i))
                    continue
                tempcount=countpattern(text,l+1,i+1)
                count+=tempcount
                d[(l,i)]=tempcount
        return count
    else:
        return 0
            
    
def main():
    global sequence,num
    l=set()
    existletters=''
    for i in range(len(sequence)):
        l.add(sequence[i])
    for i in range(len(l)):
        existletters+=l.pop()
    pattern='[^'+existletters+']*'
    p=re.compile(pattern)
    for case in range(input()):
        count=0
        d.clear()
        text=raw_input()
        text=p.sub('',text)
        count=countpattern(text,0,0)
        outcount='0000'+str(count)
        print 'Case #%d: %s' % (case + 1, outcount[-4:])

sequence=['w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m']
d = defaultdict(int)
main()