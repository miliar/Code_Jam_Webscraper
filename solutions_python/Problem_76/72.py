name = "C-large"
f_in = open(name + '.in',"r")
f_out = open(name + '.out','w')



def findMinIndex(l):
        i = 0
        for j in range(1,len(l)):
                if(l[j] < l[i]):
                        i = j
        return i

def xorAll(l):
        x = 0
        for y in l:
                x = x ^ y
        return x

T  =  int(f_in.readline())    
for i in range(T):
        N = int(f_in.readline())    
        l = [int(x) for x in (f_in.readline().split())]
       
        if(len(l) == 0 or xorAll(l) != 0):        
                f_out.write("Case #" +str(i+1) + ": "+ str("NO")+"\n")
        else:
                f_out.write("Case #" +str(i+1) + ": "+ str(sum(l) - l[findMinIndex(l)])+"\n")
 

f_in.close()
f_out.close()
