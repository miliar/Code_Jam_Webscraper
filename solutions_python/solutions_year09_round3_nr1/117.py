'''
Created on 13-sep-2009

@author: pbruyn0
'''


def processfile(inname,outname):
    infile = open(inname,'r')
    lines = infile.readlines()
    infile.close()
    N=int(lines[0].strip())
    outfile = open(outname,'w')
    for cnt in range(1,N+1):
        strval = lines[cnt].strip()
        result = minbaseval(strval)
        outfile.write('Case #'+str(cnt)+': '+str(result)+'\n')
    outfile.close()
    
def minbaseval(strval):
    if len(strval)==1:
        return 1
    strlen = len(strval)
    setval = set(strval)
    base = max(len(setval),2)
    v = [1,0]+list(range(2,40))
    valdict={}
    result = 0
    for i,s in enumerate(strval):
        if valdict.has_key(s):
            result += valdict[s]*base**(strlen-i-1)
        else:
            valdict[s] = v.pop(0)
            result += valdict[s]*base**(strlen-i-1)
    return result
    