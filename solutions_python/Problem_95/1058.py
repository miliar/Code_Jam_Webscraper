dicts = {}
outstr = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
instr  = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
i=0
for char in instr:
    dicts[char]=outstr[i]
    i+=1
dicts['z'] = 'q'
dicts['q'] = 'z'

fin = open("./A-small-attempt0.in",'r')
fout = open("./output.out",'w')
n = int(fin.readline())
for i in range(1,n+1):
    inline = fin.readline()
    outline = "Case #" + str(i)+": "
    for char in inline:
        if(char!="\n"):outline += dicts[char]
    outline+="\n"
    fout.write(outline)

fin.close()
fout.close()
        
