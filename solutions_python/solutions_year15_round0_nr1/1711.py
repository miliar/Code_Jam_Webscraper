def solve(Smax, S):
    count = 0
    add_count = 0
    
    for i, c in enumerate(S):
        #print(i,c)
        if c == 0 or count >= i:
            count += c
        else:
            diff = i - count
            count += diff + c
            add_count += diff
            #print("added {}".format(diff))

    return add_count

def main(file):
    with open(file+".in") as fin:
        with open(file+".out","w") as fout:
            T = int(fin.readline().strip())
            for n in range(1,T+1):
                Smax, S = fin.readline().split()
                out = solve(int(Smax), [int(x) for x in S])
                fout.write("Case #{}: {}\n".format(n,out))

if __name__ == "__main__":
    main("A-large")
