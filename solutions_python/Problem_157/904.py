fin=open("C:/codejam/2015/C/C-small-attempt2.in","r")
fout=open("C:/codejam/2015/C/C-small-attempt2.out","w")

products = {
    "11":[1,"1"],
    "1i":[1,"i"],
    "1j":[1,"j"],
    "1k":[1,"k"],
    "i1":[1,"i"],
    "ii":[-1,"1"],
    "ij":[1,"k"],
    "ik":[-1,"j"],
    "j1":[1,"j"],
    "ji":[-1,"k"],
    "jj":[-1,"1"],
    "jk":[1,"i"],
    "k1":[1,"k"],
    "ki":[1,"j"],
    "kj":[-1,"i"],
    "kk":[-1,"1"]
    }

def prod(q1,q2):
    #print("q1 "+str(q1))
    #print("q2 "+str(q2))
    sign=q1[0]*q2[0]
    string=q1[1]+q2[1]
    #print(string)
    temp_res=products[string]
    sign = sign*temp_res[0]
    #print(temp_res)
    res = [sign,temp_res[1]]
    return res

def string_prod(s):
    current_prod=[1,s[0]]
    #print(s)
    for i in range(1,len(s)):
        current_prod=prod(current_prod,[1, s[i]])
    if(current_prod[0]==1):
        return current_prod[1]
    else:
        return "A"

def find_invers(total,a,c):
    #print("a "+str(a))
    #print("c "+str(c))
    #print("big_total "+str(total))
    for sign in [1,-1]:
        for lit in ["1","i","j","k"]:
            ab=prod(a,[sign, lit])
            abc=prod(ab,c)
            if(abc[0]==total[0] and abc[1]==total[1]):
                    return [sign, lit]
    return "diofa"
        
##q1=[1,"j"]
##q2=[-1,"k"]
##q3=[1,"i"]
##
##print(prod(q1,q2))
##print(prod(q2,q2))
##print(prod(q2,q3))
##print(prod(q3,q1))

T=int(fin.readline())

for case in range(1,T+1):
    L, X = [int(x) for x in fin.readline().rstrip('\r\n').split(' ')]
    tstring=fin.readline().rstrip('\r\n')
    #print(tstring)
    string=tstring*X
    #print(string)
    result="NO"
    if(len(string)<3):
        fout.write("Case #"+str(case)+": "+"NO"+"\n")
        continue
    #counter1 é START seconda stringa
    #counter2 é START terza stringa
    found=False
    current_first_prod=[1,""]

    first_product=[1,""]
    third_product=[1,""]
    big_total=[1,""]
    possible_first=[]
    possible_third=[]
    latest_third=-1
    for cc in range(len(string)-1,0,-1):
        if(cc==len(string)-1):
            third_product=[1, string[len(string)-1]]
        else:
            third_product=prod([1, string[cc]],third_product)
        if(third_product[0]==1 and third_product[1]=="k"):
            latest_third=cc
            break
    least_first=len(string)+1
    for cc in range(0,len(string)):
        if(cc==0):
            first_product=[1, string[0]]
        else:
            first_product=prod(first_product,[1, string[cc]])
        if(first_product[0]==1 and first_product[1]=="i"):
            least_first=cc
            break

    for cc in range(0,len(string)):
        if(cc==0):
            big_total=[1,string[0]]
        else:
            big_total=prod(big_total,[1,string[cc]])
    
    if(least_first>latest_third):
        fout.write("Case #"+str(case)+": "+"NO"+"\n")
        continue
    inmezzo=find_invers(big_total,[1,"i"],[1,"k"])
    if(inmezzo[0]==1 and inmezzo[1]=="j"):
        fout.write("Case #"+str(case)+": "+"YES"+"\n")
        continue
    else:
        fout.write("Case #"+str(case)+": "+"NO"+"\n")
        continue
fin.close()
fout.close()
