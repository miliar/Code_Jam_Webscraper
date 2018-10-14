
from collections import *
from copy import *
from math import *
from fractions import *

if __name__=='__main__':
    input=open('C-small-attempt3.in.txt','r+')
    output=open('C-small-attempt3.out.txt','w+')

    numCases = int(input.readline().strip())
    for case in range(1,numCases+1):
        [c,d,v]=input.readline().strip().split()
        c=int(c)
        d=int(d)
        v=int(v)

        values = set()
        for i in range(1,v+1):
            values.add(i)
        coins =input.readline().strip().split()
        cc=set()
        for i in range(d):
            coins[i]=int(coins[i])
            cc.add(coins[i])

        use = []
        for i in range(d):
            use.append(0)

        possibles=[]
        choices = int(pow(2,d))
        for i in range(1,choices):
            use[0]+=1
            index=0
            while use[index]==2:
                use[index+1]+=1
                use[index]=0
                index+=1
            value = 0
            for i in range(d):
                value+=use[i]*coins[i]
            if value<=v:
                possibles.append(value)
                if value in values:
                    values.remove(value)

        #print possibles
        result = 0
        while len(values)!=0:
            result+=1
            newCoin = min(list(values))
            coins.append(newCoin)
            d=d+1
            choices = int(pow(2,d))
            use=[]
            for i in range(d):
                use.append(0)
            for i in range(1,choices):
                use[0]+=1
                index=0
                while use[index]==2:
                    use[index+1]+=1
                    use[index]=0
                    index+=1
                value = 0
                for i in range(d):
                    value+=use[i]*coins[i]
                    if value<=v:
                        possibles.append(value)
                        if value in values:
                            values.remove(value)

            
        
        #print case
        output.write("Case #%d: %d\n"%(case,result))
        

    input.close()
    output.close()