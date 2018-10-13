file = open("codejam1large.txt","r")
t = int(file.readline())
out = open("1large.txt","w")
for k in range(t):
    smax,string = file.readline().split()
    people = list(string)
    needed =0
    standing = 0
    for i in range(int(smax)+1):
        if standing>=i:
            #if enough people stand
            standing+=int(people[i])
        else:
            needed +=i-standing
            standing = i+int(people[i])
    out.write("Case #"+str(k+1)+": "+str(needed)+"\n")
out.close()
