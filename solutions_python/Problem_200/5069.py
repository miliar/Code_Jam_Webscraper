r_fname="B-small-attempt1.in"
w_fname="output_small.txt"
with open(r_fname,"r") as file:
    contents=file.readlines()
with open(w_fname,"w+") as file:
    t=int(contents[0].strip("\n"))
    for j in range(1,t+1):
        n=contents[j]
        for i in range(int(n),-1,-1):
            l=list(str(i))
            l1=sorted(l)
            if l1==l:
                file.write("Case #%d: %d\n"%(j,i))
                break
        
        
