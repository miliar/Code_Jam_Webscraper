'''
Created on May 22, 2010

@author: mogox
'''
dbg=True
outfilename= 'a-large.out'
outfile = open(outfilename, 'w+')

def log(str):
    if(dbg):
        print str
    
def write(str):
    print str
    outfile.write(str+"\n")

t=int(raw_input())
for i in range(t):
    line= raw_input()
    values=line.strip().split(" ")
    n=int(values[0])
    m=int(values[1])
    dirs={}
    dirs['/']=True
    for j in range(n):
        line=raw_input()
        line=line.lstrip('/')
        fs=line.split('/')
        path= ''
        for name in fs:
            path+='/'+name
            dirs[path]=True
    t=0
    for j in range(m):
        line=raw_input()
        line=line.lstrip('/')
        fs=line.split('/')
        path= ''
        for name in fs:
            path+='/'+name
            if(dirs.has_key(path)):
                continue
            else:
                dirs[path]=True
                t+=1
    write('Case #'+str(i+1)+': '+str(t))