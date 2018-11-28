import os,math,sys,re




def getNum(x,a,b):
    if ( (a*b)%x != 0):
        return 0
    if x == 1:
        return 1
    d=[212,214,222,223
    ,323
    ,224
    ,333
    ,234
    ,334
    ,434
    ,244
    ,344
    ,444]

    num= x*100+a*10 +b
    if num in d:
        return 1
    else:
        return 0



temp="";

f = open("C:/Users/Quan/Desktop/google_code_jam2015/D-small-attempt2.in","r")

T=int(f.readline());

for i in range(0,T):
    line=f.readline();
    j = i + 1;
    x = int(line[0])
    r = int(line[2])
    c = int(line[4])

    res = getNum(x,min(r,c),max(r,c))
    if (res == 1):
        temp += "Case #" + str(j)+": GABRIEL\n"
    else:
        temp += "Case #" + str(j)+": RICHARD\n"

outfile=open("C:/Users/Quan/Desktop/google_code_jam2015/sample_d.out","w")
outfile.write(temp)
outfile.close()
f.close()

