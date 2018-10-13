def deter(k):
    k = str(k)
    if len(k) == 1:
        return int(k)
    return gen(k)

def gen(k):
    for i in range(len(k)-1):
        if k[i] > k[i+1]:
            r = k[0:i]
            end = str(int(k[i])-1)+(len(k)-i-1)*"9"
            r = r+end
            return gen(r)
    return int(k)
        

def main():
    m = int(input(""))
    rlist = []
    for i in range(m):
        p = input("")
        rlist.append(deter(p))
    for j in range(len(rlist)):
        print("Case #{}: {}".format(j+1,rlist[j]))

if __name__ == "__main__":
    main()

