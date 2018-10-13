import string

ifile = open("A-large.in")
s = ifile.read().split("\n")
ifile.close()

T = int(s[0])

out = []
for i in range(1,T+1):
    N = int(s[i].split(" ")[0])
    K = int(s[i].split(" ")[1])

    if (K+1)%pow(2,N)==0:
        O = "ON"
    else:
        O = "OFF"
    
    out.append("Case #"+str(i)+": "+O)

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()