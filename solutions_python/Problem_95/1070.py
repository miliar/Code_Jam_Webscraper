'''
Created on 14-04-2012

@author: Hokanos
'''
import sys
def replace(S,D):
    r = "";
    for i in range(len(S)):
        if S[i] != " ":
            r+= D[S[i]]
        else:
            r+= " ";
    return r.lstrip();
    
def main():
    stra = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    strb = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    dict = {}
    dictb = {}#normal to coded
    tab = {}
    slowo = ""
    aplh = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".lower()
    for x in range(len(stra)):
        if stra[x] == " ":
            continue
        dict[stra[x]] =  strb[x]
        dictb[strb[x]] =  stra[x]

    dict["y"] = "a"
    dict["q"] = "z"
    dictb["a"] = "y"
    dictb["z"] = "q"
    
    
    for i in range(len(aplh)):
        if aplh == " ":
            continue
        if aplh[i] in dictb:
            tab[aplh[i]] = dictb[aplh[i]]
        else:
            tab[aplh[i]] = "z"
            
    # 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'
    a = {}
    for x in tab:
        if ord(x) != 32:
            print(tab[x])
            a[tab[x]] = x
    
    print(a.keys())
    
    f = open(sys.argv[1],"r")
    fw = open("out.out","w")
    
    line = f.readline()
    nums = int(line)
    
    for i in range(nums):
        fw.write("Case #"+str(i+1)+": "+replace(f.readline().rstrip(),a)+"\n")
    
    f.close()
    fw.close()

main()