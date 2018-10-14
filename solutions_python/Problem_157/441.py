#coding:utf-8

#四元数


def multi(b,a):#a*b
    dic={"11":"1", "1i":"i", "1j":"j", "1k":"k","i1":"i", "ii":"-1","ij":"-k", "ik":"j","j1":"j", "ji":"k", "jj":"-1", "jk":"-i","k1":"k", "ki":"-j", "kj":"i", "kk":"-1"}
    sign=["","-"]
    signflag=0
    if a[0]=="-":
        signflag=signflag+1
        a=a[1]
    if b[0]=="-":
        signflag=signflag+1
        b=b[1]
    res=dic[a+b]
    if res[0]=="-":
        signflag=signflag+1
        res=res[1]
    return sign[signflag%2] + res

def convert(tmpstring):
    tmpc=tmpstring[0]
    for c in tmpstring[1:]:
        tmpc=multi(tmpc,c)
    return tmpc

def main():
    fr=open("C-small-attempt2.in","r")
    output=""
    ans=[]
    casenum=0
    count=0
    for line in fr:
        if count==0:
            casenum=int(line)
        else:
            if (count%2) == 1:#繰り返し回数
                repeatnum=int(line.split()[1])
            else:
                print(len(ans))
                tmpans=False
                stringdata=(line.replace("\n","")*repeatnum)
                #前から順に読んで、iが作れたら残りでj,kを作れるか
                current_index=1
                tmp=stringdata[0]
                #ijkになる最低条件
                if convert(stringdata)=="-1":
                    for c in stringdata[1:]:
                        if tmp=="i":#これより先でj,kを作れるか
                            tmpchar=stringdata[current_index]
                            current_index2=current_index+1
                            for c2 in stringdata[(current_index+1):]:
                                if tmpchar=="j":#ここより先でkを作れるか
                                    if convert(stringdata[current_index2:])=="k":
                                        tmpans=True
                                        break
                                tmpchar=multi(tmpchar,c2)
                                current_index2=current_index2+1
                            break
                        tmp=multi(tmp,c)
                        current_index=current_index+1
                if tmpans:
                    ans.append("YES")
                else:
                    ans.append("NO")
        count=count+1

    for i in range(0,casenum):
        output=output+"Case #"+str(i+1)+": "+str(ans[i])+"\n"

    fr.close()


    fw=open("out.txt","w")
    fw.write(output)
    fw.close()

main()