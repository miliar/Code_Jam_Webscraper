import re,sys

def process_data(filename,opfile):
    f=open(filename)
    fout=open(opfile,'w')
    lineno=0
    cases,curr=0,0
    for line in f:
        lineno+=1
        line=line.strip()
        if(lineno==1):
            cases=int(line)
            continue
        curr+=1
        print curr
        fout.write('Case #%d: %d\n'%(curr,mintime(line)))
        fout.flush()
    fout.close()
    f.close()
def dist(s):
    return len(set(list(s)))


def mintime(s):
    base=dist(s)
    if(base==1):base=2 #whew!
    sym={}
    digval=1
    num=[]
    for elem in list(s):
        if(sym.has_key(elem)):
            num.append(sym[elem])
        else:
            sym[elem]=digval
            if(digval==1):
                digval=0
            elif(digval==0):
                digval=2
            else:digval+=1
            num.append(sym[elem])
    print num
    time=0
    for i in range(1,len(num)+1):
        idx=-1*i
        #print pow(base,i-1),base
        time+= pow(base,i-1)*num[idx]
        #print time
    return time
