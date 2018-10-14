myDic={}
line1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
out1="our language is impossible to understand"
line2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
out2="there are twenty six factorial possibilities"
line3="de kr kd eoya kw aej tysr re ujdr lkgc jv"
out3="so it is okay if you want to just give up"

lines=line1+line2+line3
outs=out1+out2+out3

for i in range(len(lines)):
    if lines[i] not in myDic:
        myDic[lines[i]]=outs[i]
myDic['z']='q'
myDic['q']='z'

f=open(input("filename"))
o=open("output.txt","w")
t=int(f.readline())
line=f.readline()
i=1
while line:
    outLine="Case #%d: "%i
    for letter in line:
        if letter in myDic:
            outLine+=myDic[letter]
        else:
            outLine+=letter
            #print(letter)
    o.write(outLine)
    i+=1
    line=f.readline()
f.close()
o.close()
    

