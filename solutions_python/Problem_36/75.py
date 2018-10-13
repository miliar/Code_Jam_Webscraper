# code jam C

#cacheing...

import re

cache={}

def ways(target,fromletters):
    if not(target):
        return 1
    else:
        key=target+'@@@@@'+fromletters
        if key in cache:
            return cache[key]
        else:
            firstletter=target[0]
            places=[i for i in range(len(fromletters))
                    if firstletter==fromletters[i]]
            if places:
                ans=sum([ways(target[1:],fromletters[p+1:])
                           for p in places])
            else:
                ans=0
            cache[key]=ans
            return ans
        
datain="""
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam
"""
datain=open("C-large.in").read()

dataout=open("C-large.out","w")


data=[x for x in datain.split('\n') if x]

for i,d in enumerate(data[1:]):
    cache={}
    text='Case #'+str(i+1)+': '+str(10000+ways("welcome to code jam",d))[-4:]
    dataout.write(text+'\n')
    print text

dataout.close()
    
