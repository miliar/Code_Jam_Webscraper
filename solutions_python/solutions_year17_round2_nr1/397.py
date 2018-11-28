#fi=open("C:\\users\\Sergiy\\Downloads\\A-small-attempt0.in",'r')
fi=open("C:\\users\\Sergiy\\Downloads\\A-large.in",'r')
fo=open("answer.txt",'w')

def calc(): 
    D,N=map(int,fi.readline().strip().split())
    T=0    
    for i in range(N):
        k,s=map(int,fi.readline().strip().split())
        if k>=D: continue
        if (D-k)/s>T: T=(D-k)/s
    return '{:.9f}'.format(D/T)
        
for testNo in range(int(fi.readline())): 
    print("Case #{}: {}".format(testNo+1,calc()),file=fo)
    print(testNo)

fi.close()
fo.close()
print("Ok")