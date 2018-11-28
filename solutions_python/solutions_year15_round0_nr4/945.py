def solve(X, R, C):
    res = 0
    if X == 1:
        res = 1
    elif X == 2:
        if (R*C) % 2 == 0:
            res = 1
    elif X == 3:
        if (R*C) in (6, 9, 12):
            res = 1
    elif X == 4:
        if (R*C) in (12, 16):
            res = 1
    else:
        print("X>4", X)
   
    return "GABRIEL" if res == 1 else "RICHARD"
    
def main(file):
    with open(file+".in") as fin:
        with open(file+".out","w") as fout:
            T = int(fin.readline().strip())
            for n in range(1,T+1):
                X, R, C = [int(x) for x in fin.readline().split()]
                out = solve(X, R, C)
                fout.write("Case #{}: {}\n".format(n,out))

if __name__ == "__main__":
    main("D-small-attempt0")
