def toggle(a):
    if(a):return 0
    else:return 1

def snap(n,k):
    state = [0]*n
    final = [[1]*n]
    x = 0
    while state not in final:
        state = [toggle(i) for i in state[:state.index(0)+1]]+state[state.index(0)+1:]
        x+=1
    if x<=k:
        if (k+1)%(x+1)>0:
            return "OFF"
        else:return "ON"
    else:
        return "OFF"
input = open("A-small-attempt2.in","r")    
output = open("A-small-attempt2.out","w+")
nol = input.readline()
z = 1
for i in range(int(nol)):
    fl = input.readline().split()
    ri = snap(int(fl[0]),int(fl[1]))
    output.write("Case #"+str(z)+": "+str(ri)+"\n")
    z+=1
    