import sys
sys.path.append("..")
import codejam as cj
from random import randint

cj.name="magic_trick"

data=cj.read(".txt")
#data=["3","2","1 2 3 4","5 6 7 8","9 10 11 12","13 14 15 16"]

''''
def shuffle(data):
    temp=[]
    for i in range(1,17):
        temp.insert(randint(0,15),i)
    ret=[]
    for i in range(0,4):
        ret.append(temp[i*4:(i+1)*4])
    return ret'''
    
def intersect(l1,l2):
    if l1==[]:
        return l2
    return [a for a in l1 if a in l2]

cases=int(cj.getNext(1,data))
pos=1
result=""
count=1
for i in xrange(0,cases):
    ans=cj.getNext(1,data)
    while ans!=-1:
        result+="Case #"+str(count)+": "
        count+=1
        known=[]
        for j in range(0,2):
            cards=cj.getNext(4,data)
            #print ans,cards,cards[int(ans)-1].split(" ")
            known=intersect(known,cards[int(ans)-1].split(" "))
            #print known
            #print cards,known
            ans=cj.getNext(1,data)
        #print known,"--"
        if len(known)==1:
            result+=str(known[0])+"\n"
        elif len(known)==0:
            result+="Volunteer cheated!\n"
        else:
            #print known
            result+="Bad magician!\n"
            
#result=result[0:-1]
#print result
cj.finish(result)