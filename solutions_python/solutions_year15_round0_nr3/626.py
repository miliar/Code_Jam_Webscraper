__author__ = 'rainp1ng'

def main(inr,outr):
    t=int(inr.readline())
    for i in range(t):
        outr.write("Case #%s: "%(i+1)+solve(inr)+"\n")

def solve(inr):
    l=map(int,inr.readline().split())
    digits=l[0]*l[1]
    repeat=l[1]
    string=get_str(inr.readline().split()[0],repeat)
    if get_ijk(string,digits):
        return "YES"
    else:
        return "NO"

ijk_dic=["i","j","k"]
def get_ijk(string,digits):
    fail=0
    i=0
    j=0
    str_list=[""]
    while j<digits:
        if str_list[i]!=ijk_dic[i] or i==2:
            if len(str_list[i])>0 and str_list[i][0]=="-":
                op="-"
                str_list[i]=str_list[i].replace("-","")
            else:
                op=""
            mul=mul_dic[str_list[i],string[j]]
            if mul[0]=="-":
                op2="-"
                mul=mul.replace("-","")
            else:
                op2=""
            str_list[i]=get_op(op,op2)+mul
            j+=1
        elif str_list[i]==ijk_dic[i] and i<2:
            i+=1
            str_list.append("")
    if i==2 and str_list[i]==ijk_dic[i]:
        return True
    return False


def get_op(str1,str2):
    if len(str1)==0:
        return len(str2)!=0 and "-" or ""
    elif len(str2)==0:
        return len(str1)!=0 and "-" or ""
    elif (str1[0]=="-" and str2[0]!="-") or (str1[0]!="-" and str2[0]=="-"):
        return "-"
    else:
        return ""


mul_dic={
    ("","1"):"1",("","i"):"i",
    ("","j"):"j",("","k"):"k",
    ("1","1"):"1",("1","i"):"i",
    ("1","j"):"j",("1","k"):"k",
    ("i","1"):"i",("i","i"):"-1",
    ("i","j"):"k",("i","k"):"-j",
    ("j","1"):"j",("j","i"):"-k",
    ("j","j"):"-1",("j","k"):"i",
    ("k","1"):"k",("k","i"):"j",
    ("k","j"):"-i",("k","k"):"-1",
}

def get_str(string,repeat):
    res=""
    while repeat>0:
        res+=string
        repeat-=1
    return res

inr=open("/Users/rainp1ng/Downloads/Contest/GoogleCodeJam/identification_round/C-small-attempt0.in","rb")
outr=open("/Users/rainp1ng/Downloads/Contest/GoogleCodeJam/identification_round/output","wb")

main(inr,outr)
