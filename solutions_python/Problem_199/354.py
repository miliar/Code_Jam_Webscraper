def solve(s, k):
    k = int(k)
    s = [ch=="+" for ch in s]
    c = 0
    for i in range(0, len(s)):
        if s[i]:
            continue
        if i + k > len(s):
            return "IMPOSSIBLE"
        c += 1    
        for j in range(i, i+k):
            s[j] = not s[j]
    return c

    

with open("in.txt", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = lines[0]
    for i in range(1, len(lines)):
        [S,K] = lines[i].split(" ")
        ofile.write("Case #{}: {}\n".format(i, solve(S,K)))
        