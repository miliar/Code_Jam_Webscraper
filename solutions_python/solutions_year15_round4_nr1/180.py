import sys,math

class debugged(object):
    def __init__(self,func):
        self.func = func
        
    def __call__(self,*args):
        print("[{}({}) = ? ".format(self.func.__name__,args),file=sys.stderr)
        val = self.func(*args)
        print("{}({}) = {}]".format(self.func.__name__,args,val),file=sys.stderr)
        return val


def find_arrows(R,C,M):
    res = []
    for i in range(R):
        for j in range(C):
            if M[i][j] != "." :
                res.append((i,j,M[i][j]))
    return res

D={}
D["^"]=(-1,0)
D["v"]=(1,0)
D[">"]=(0,1)
D["<"]=(0,-1)

dirs = [(-1,0),(1,0),(0,1),(0,-1)]

#@debugged
def is_arrow_in_dir(R,C,M,i,j,d):
    di,dj = d
    ii,jj = i+di,j+dj
    while (0 <= ii < R) and (0 <= jj < C) and (M[ii][jj] == "."):
        ii += di
        jj += dj
    return (0 <= ii < R) and (0 <= jj < C)

def main(R,C,M):
    arr = find_arrows(R,C,M)
    res = 0
    for a in arr:
        i,j,da = a
        d = D[da]
        ok = [dd for dd in dirs if is_arrow_in_dir(R,C,M,i,j,dd)]
        if len(ok) == 0:
            return "IMPOSSIBLE"
        else:
            res += d not in ok
    return res

def main_2x2(R,C,M):
    arr = find_arrows(R,C,M)
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return "IMPOSSIBLE"
    elif R == 1 and C == 1:
        return "IMPOSSIBLE"
    elif R == 1 and C == 2:
        return (M[0][0] != ">") + (M[0][1] != "<")
    elif R == 2 and C == 1:
        return (M[0][0] != "v") + (M[1][0] != "^")
    else: ## 2x2
        if len(arr) == 2:
            if arr[0][0] == arr[1][0] :
                MM = [m[arr[0][0]] for m in M]
                return main_small(R,1,MM)
            elif arr[0][0] == arr[0][1]:
                MM = M[arr[0][1]]
                return main_small(R,1,MM)
        else: ## 4 arrows
            return ((M[0][0] not in [">","v"])
                    + (M[0][1] not in ["<","v"])
                    + (M[1][0] not in [">","^"])
                    + (M[1][1] not in ["<","^"]))
    
if __name__ == "__main__":
    T = int(input())
    for c in range(T):
        ## Input
        R,C = [int(i) for i in input().split()]
        M = []
        for _ in range(R):
            M.append(input())
        ## Processing
        res = main(R,C,M)
        ## Output
        print("Case #{}: {}".format(c+1,res))


