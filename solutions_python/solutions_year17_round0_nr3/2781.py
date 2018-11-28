def print_case(case, ans):
    print("Case #"+str(case)+": " + str(ans))
def find_values(n,k):
    world = ["0"]+["."] * n+["0"]
    for i  in range(k):
        maxm = 0
        minm = 0
        best = -1
        for cell in range(1,n):
            if world[cell] == ".":
                ls,rs = 0,0
                j = cell
                while(world[j] == "."):
                    ls += 1
                    j += 1
                j = cell
                while(world[j] == "."):
                    rs += 1
                    j -= 1
                if(min(rs,ls) > minm):
                    best = cell
                    minm = min(rs,ls)
                    maxm = max(rs,ls)
                elif(min(rs,ls) == minm) and (max(ls,rs) > maxm):
                    best = cell
                    minm = min(rs,ls)
                    maxm = max(rs,ls)
        world[best] = "0"
    if maxm == 0 and minm == 0:
        return 0,0
    return maxm-1,minm-1
def main():
    t = int(input())
    for i in range(t):
        raw = input().split()
        n = int(raw[0])
        k = int(raw[1])
        max,min = find_values(n,k)
        print_case(i+1,str(int(max))+" "+str(int(min)))
main()