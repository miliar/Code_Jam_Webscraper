import os,math,sys,re

def getNum(array):
    N = len(array)
    res = 0
    s =0
    for i in range(0,N):
        if ( i -s > res):
            res=i-s
        s = s+array[i]
    return res


temp="";

f = open("C:/Users/Quan/Desktop/google_code_jam2015/A-large.in","r")

T=int(f.readline());

for i in range(0,T):
    line=f.readline();
    j = i + 1;
    LEN = int(re.split(" ",line)[0])
    k=2
    if LEN < 10:
        k = 2
    elif LEN < 100 :
        k = 3;
    elif LEN < 1000:
        k = 4
    else:
        k = 5
        
    array=[]
    for counter in range(k, k+LEN+1):
        array.append(int(line[counter]))
    res = getNum(array)
    temp += "Case #" + str(j)+": " +str(res) + "\n"

outfile=open("C:/Users/Quan/Desktop/google_code_jam2015/sample_a.out","w")
outfile.write(temp)
outfile.close()
f.close()

