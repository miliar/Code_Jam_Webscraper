import copy
def change(k:list,l:int,rd:int):

    if rd > 500:
        return str("IMPOSSIBLE")
    
    if "+"*len(k[0]) in k:
        return rd

    rlist = []
    
    for j in range(len(k)):
        kitem = k[j]
        for i in range(len(kitem)-l+1):
            nslice = copy.copy(kitem[i:i+l])
            nslice = nslice.replace("-","0").replace("+","-").replace("0","+")
            new = kitem[0:i] + nslice + kitem[i+l:]
            rlist.append(new)

    rlist = list(set(rlist))

    rd += 1
    return change(rlist,l,rd)

def main():
    alist = []
    s = int(input(""))
    for i in range(s):
        o =  input("").split()
        g,c = o[0],int(o[1])
        alist.append(change([g],c,0))

    for j in range(len(alist)):
        print("Case #{}: {}".format(j+1,alist[j]))


if __name__ == "__main__":
    main()
    
        
        
        
