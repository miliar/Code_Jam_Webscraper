with open("A-large.in") as f:
    input_Arr = f.readlines()
with open("output.txt","w") as g:
    for q in range(int(input_Arr[0])):
        inp=input_Arr[q+1].split(' ')
        cur=0
        needed=0
        for c in range(len(inp[1])-1):
            cur+=int(inp[1][c])
            if (c+1)>cur:
                needed+=1
                cur+=1
        outp='Case #'+str(q+1)+': '+str(needed)+'\n'
        g.write(outp)
            
        

