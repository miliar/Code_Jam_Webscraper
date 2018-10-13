with open("B.out","w") as fout:
    with open("B.in") as fin:
        for t in range(int(fin.readline())):
            n = list(map(int,fin.readline().strip()))
            while 1:
                o = []
                for i in range(len(n)):
                    if i==len(n)-1 or n[i]<=n[i+1]:
                        o.append(n[i])
                    else:
                        o+=[n[i]-1]
                        o+=[9]*(len(n)-i-1)
                        break
                else:
                    fout.write("Case #"+str(t+1)+": "+"".join(map(str,o)).lstrip("0")+"\n")
                    break
                n=o
