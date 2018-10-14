
#sample
In=["ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
Out=["our language is impossible to understand",
     "there are twenty six factorial possibilities",
     "so it is okay if you want to just give up"]

def main():

    mapp=[' ' for j in range(0,26)]
    ecovered=[0 for i in range(0,26)]
    
    mapp[ord('y')-97]='a'
    ecovered[ord('a')-97]=1
    
    mapp[ord('e')-97]='o'
    ecovered[ord('o')-97]=1
    
    mapp[ord('q')-97]='z'
    ecovered[ord('z')-97]=1
    
    for k in range(0,3):
        gletters=list(In[k])
        eletters=list(Out[k])
        for i in range (0,len(gletters)):
            if(gletters[i]!=' ' and ( mapp[ord(gletters[i])-97]==' ')):
                mapp[ord(gletters[i])-97]=eletters[i]
                ecovered[ord(eletters[i])-97]=1
    for i in range(0,26):
        if(mapp[i]==' '):
            for j in range(0,26):
                if(ecovered[j]==0):
                    mapp[i]=chr(97+j)
                    break
            break

    fin=open("A-small-attempt2.in",'r')
    fout=open("output.out",'w')
    length=fin.readline().strip()
    case=1
    for line in fin.readlines():
        gstr=list(line.strip())
        estr=[' ' for j in range(0,len(gstr))]
        for i in range(0,len(gstr)):
            if(gstr[i]==' '):
                estr[i]=' '
            else:
                estr[i]=mapp[ord(gstr[i])-97]

        fout.write("Case #"+str(case)+": "+''.join(estr)+"\n")
        case+=1


if __name__ == '__main__':
        main()
