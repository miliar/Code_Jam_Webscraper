g1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
g2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
g3="de kr kd eoya kw aej tysr re ujdr lkgc jv"

n1="our language is impossible to understand"
n2="there are twenty six factorial possibilities"
n3="so it is okay if you want to just give up"

codebook={}
code_list=[(g1,n1),(g2,n2),(g3,n3)]
for (code,normal) in code_list:
    print code,normal
    for j in range(len(code)):
        if code[j] not in codebook.keys():
            codebook[code[j]]=normal[j]
        else:
            if codebook[code[j]]!=normal[j]:
                print "error",code[j],codebook[code[j]],normal[j]




codebook['q']='z'        
codebook['z']='q'        
for c in codebook.keys():
    print c,":",codebook[c]


infile=open("A-small-attempt1.in")
        
print len(codebook.keys())
print len(codebook.values())
print sorted(codebook.keys())
print sorted(codebook.values())
outfile=open("output.txt","w")
count=1
cases=infile.readline()
for code in infile:
    print code
    outfile.write("Case #"+str(count)+": ")
    count+=1
    normal=[]
    for j in range(len(code)):
        if code[j]!='\n':
            outfile.write(str(codebook[code[j]]))
    outfile.write("\n")
outfile.close()
