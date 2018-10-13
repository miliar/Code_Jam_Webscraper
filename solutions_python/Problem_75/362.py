'''
Created on Oct 19, 2009

@author: sg0892495
'''
import string

dynamicMap={}

def converse():
    mixtures={}
    opsite=set()
    line= file.readline().split()
    size=string._int(line[0])
    del line[0]
    for i in range(0,size):
        mixture=line[0]
        del line[0]
        mixtures[(mixture[0],mixture[1])]=mixture[2]
        mixtures[(mixture[1],mixture[0])]=mixture[2]
    size=string._int(line[0])
    del line[0]
    for i in range(0,size):
        op=line[0]
        del line[0]
        opsite.add((op[0],op[1]))
        opsite.add((op[1],op[0]))
    del line[0]
    ingreedmentsInside={}
    result=[]
    for move in line[0]:
        if(len(result)==0):
            result.append(move)
            ingreedmentsInside[move]=1
        else:
            if(mixtures.has_key((result[-1],move))):
                newKey=mixtures[(result[-1],move)]
                if(ingreedmentsInside[result[-1]]==1):
                    ingreedmentsInside.pop(result[-1])
                else:
                    ingreedmentsInside[result[-1]]-=1
                del result[-1]
                result.append(newKey)
                if(ingreedmentsInside.has_key(newKey)):
                    ingreedmentsInside[newKey]+=1
                else:
                    ingreedmentsInside[newKey]=1
            else:
                result.append(move)
                if(ingreedmentsInside.has_key(move)):
                    ingreedmentsInside[move]+=1
                else:
                    ingreedmentsInside[move]=1
            for key in ingreedmentsInside.keys():
                if((key,result[-1]) in opsite):
                    result=[]
                    ingreedmentsInside={}
                    break            
    return str(result).replace('\'', '')
    
    
    

                 

file = open('./a2.in')
for i in range(0,string._int(file.readline())):
    print 'Case #%s: %s' %((i+1), converse())

