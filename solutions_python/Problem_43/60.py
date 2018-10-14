def get_base(word):
    s=set()
    count=0
    for i in word:
        if i not in s:
            s.add(i)
            count+=1
    if count==1:
        return 2
    return count


def compute(d,base):
    power=0
    suma=0
    d.reverse()
    for k in d:
        suma+=k*base**power
        power+=1
    return suma
        
def get_sec(word):
    base=get_base(word)
    d=[]
    s={}
    if len(word)==1:
        return 1
    else:
        d.append(1)
        s[word[0]]=1
        i=1    
        while i<len(word) and word[i]==word[0]:
            d.append(1)
            i+=1
        if i==len(word):
            return compute(d,base)
        else:
            d.append(0)
            s[word[i]]=0
            i+=1
            value=2
            while i<len(word):
                if word[i] not in s:
                    s[word[i]]=value
                    d.append(value)
                    value+=1
                    i+=1
                else:
                    d.append(s[word[i]])
                    i+=1
            return compute(d,base)
                
        

def main():
    f=open("Alarge.in","r")
    lines=f.readlines()
    outfile = open("test_result.out", 'w')
    T=int(lines[0])
    for i in xrange(1,T+1):
        word=lines[i][:-1]
        result=get_sec(word)
        print "Case #" +str(i)+": "+str(result)
        outfile.write('Case #'+str(i)+': '+str(result)+'\n')
        
    
    
if __name__ == "__main__":
    main()
        
