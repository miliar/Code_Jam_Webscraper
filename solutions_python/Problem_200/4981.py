def check(n):
    for i in range(n,0,-1):
        k=str(i)
        for j in range(0,len(k)-1):
            if k[j]<=k[j+1]:
                continue
            break
        else:
            return i

new_path = '/Users/Balaji/AppData/Local/Temp/output.txt'
path = '/Users/Balaji/AppData/Local/Temp/B-small-attempt5.in.txt'
txt_file2=open(new_path,'w')
txt_file=open(path,'r')
a=txt_file.readlines()
for i in range(1,len(a)):
    test=check(int(a[i]))
    s="Case #"+str(i)+': '
    asdf=s+str(test)+'\n'
    txt_file2.write(asdf)
txt_file.close()
txt_file2.close()
