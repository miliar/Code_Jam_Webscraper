import time
def main():
    subseq="welcome to code jam"
    f=open("test.in","r")
    lines=f.readlines()
    N=int(lines[0][:-1])
    outfile = open("test_result.out", 'w')
    for i in xrange(1,N+1):
        string = lines[i][:-1]
        result= count(string,subseq)
        print "Case #" +str(i)+": "+format(result)
        outfile.write('Case #'+str(i)+': '+format(result)+'\n')
    f.close()
    outfile.close()
        
def format(result):
    s=str(result)
    return '0'*(4-len(str(s)))+s

class memoize(object):
    def __init__(self,function):
        self.memory={}
        self.function=function
    def __call__(self,*args):
        if args in self.memory: return self.memory[args]
        r=self.function(*args)
        self.memory[args]=r
        return r

@memoize
def count(string,subseq):
    #t=time.time()
    c=0
    if len(subseq)==1:
        for i in string:
            if i==subseq:
                c+=1
        return c%10**4
    else:
        d=generate_pos(string,subseq)
        #print time.time()-t
        ch = subseq[0]
        if d[ch]==[]:
            return 0
        else:
            for j in d[ch]:
                c+=count(string[j+1:],subseq[1:])%10**4
                #print time.time()-t
            return c%10**4
        
        
def generate_pos(string,subseq):
    dic={}
    for i in subseq:
        dic[i]=[]
    l=len(string)
    for i in xrange(l):
        current=string[i]
        if dic.has_key(current):
            dic[current].append(i)
    return dic
            
    
if __name__== "__main__":
    main()
    
    
