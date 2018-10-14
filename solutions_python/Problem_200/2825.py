fin=open("B-large.in","r")
fout=open("B-large.out","w")
fread=fin.readline

d={'9': '8', '7': '6', '1': '0', '4': '3', '6': '5', '2': '1', '0': '0', '5': '4', '3': '2', '8': '7'}

for tcase in range(1,int(fread().strip())+1):
    s=list(fread().strip())
    for i in range(len(s)-1,0,-1):
        if s[i]<s[i-1]:
            s[i-1]=d[s[i-1]]
            for j in range(i,len(s)):
                if s[j]=='9':
                    break
                s[j]='9'

    print("Case #%d: %d"%(tcase,int("".join(s))),file=fout)

fin.close()
fout.close()