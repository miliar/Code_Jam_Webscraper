dswap = {"+": "-", "-": "+"}
def swap(com, k):
    return "".join(dswap[c] for c in list(com[:k-1])) + com[k-1:]

        
def solve(c, k):
    if len(c) == k:
        if c == "+" * k:
            return 0
        elif c == "-" * k:
            return 1
        else: 
            return -1
            
    if c[0] == "+":
        mov = solve(c[1:], k)
        return solve(c[1:], k)
    else:
        mov = solve(swap(c[1:], k), k)
        if mov == -1:
            return -1
        else:
            return mov + 1




res = []
with open("A-small-attempt0.in") as f:
    t = int(f.readline().strip())
    print t
    for r in range(t):
        row = f.readline().strip()
        comb, n = row.split(" ")
        n = int(n)
        # print comb, n, solve(comb, n)
        res.append(solve(comb, n))
        
with open("out.txt", "w") as out:
    for i, r in enumerate(res):
        out.write("Case #{}: {}\n".format(i+1, str(r) if r > -1 else "IMPOSSIBLE"))
