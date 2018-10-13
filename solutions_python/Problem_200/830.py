#fi=open("C:\\users\\Sergiy\\Downloads\\B-small-attempt0.in",'r')
#fo=open("B-small-attempt0.out",'w')
fi=open("C:\\users\\Sergiy\\Downloads\\B-large.in",'r')
fo=open("B-large.out",'w')

def calc():   
    s=[0]+[int(x) for x in fi.readline().strip()]
    i=1    
    while i<len(s):
        if s[i]<s[i-1]: s[i-1]-=1; s[i:]=[9]*(len(s)-i); i-=1 
        else: i+=1
    return int(''.join(map(str,s)))
        
for testNo in range(int(fi.readline())): print("Case #{}: {}".format(testNo+1,calc()),file=fo)

fi.close()
fo.close()
print("Ok")