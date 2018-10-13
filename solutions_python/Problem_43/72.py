'''
Created on 2009/09/13

@author: hirobe
'''

def test(line):
    dic = {}
    vals = []
    for ch in line:
        if not(ch in dic.keys()):
            
            if len( dic.keys())==0:
                dic[ch]=1
            elif len(dic.keys())==1:
                dic[ch]=0
            else:
                dic[ch]=len(dic.keys())
            
            #dic[ch]=len(dic.keys())+1
        vals.append(dic[ch])
        
    base = len(dic.keys())
    if base <2 :
        base = 2
    ret = 0
    i = len(vals)-1
    #print line
    #print vals
    for val in vals:
        ret += val * (base**i)
        i -=1
    #print ret
    #print base
    #print vals
    
    return ret

def read_file():
    lines = []
    for line in open('A-large.in', 'r'):
        lines.append(line.rstrip())
    return lines[1:]

hoge = read_file()

case_index = 1
for line in read_file():
    print "Case #%d: %d"%(case_index,test(line))
    case_index += 1
    
    