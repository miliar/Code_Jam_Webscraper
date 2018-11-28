name = "D-large"
f_in = open(name + '.in',"r")
f_out = open(name + '.out','w')


def countPlace(l):
        ret = 0
        for i in range(len(l)):
                if(l[i] != i + 1):
                        ret = ret + 1
        return ret


T  =  int(f_in.readline())    
for i in range(T):
        N = int(f_in.readline())    
        l = [int(x) for x in (f_in.readline().split())]
        
        f_out.write("Case #" +str(i+1) + ": "+ str(countPlace(l))+"\n")


f_in.close()
f_out.close()
