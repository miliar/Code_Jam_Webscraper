in_file = open('B-large.in','r')
out_file = open('BoutL.txt','w')
n = int(in_file.readline())

for i in range(n):
    p=2
    t=0
    l=list(in_file.readline().split())    
    c=float(l[0])
    f=float(l[1])
    x=float(l[2])
    
    while True :
        if x/p < ((c/p)+(x/(p+f))):            
            break
        else:
            t = t+(c/p)
            p = p+f   
    
    t = t + x/p
    
    out_file.write("Case #" + str(i+1) +": " + str(t) + "\n")

out_file.close()
in_file.close()
