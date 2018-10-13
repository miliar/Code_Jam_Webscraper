def solve(v):
    v = [int(ch) for ch in v]
    if len(v) == 1:
        return v[0]
        
    for digits_kept in reversed(range(0, len(v) + 1)):
        if len(v) > digits_kept and v[digits_kept] == 0:
            continue
        
        v2 = v[:]
        if digits_kept < len(v):
            if digits_kept == 0 and v2[0]==1:
                return "".join((len(v) - 1) * "9")
            v2[digits_kept] -= 1
            for i in range(digits_kept + 1, len(v2)):
                v2[i] = 9


        tidy = True
        for i in range(1, len(v2)):
            if v2[i-1] > v2[i]:
                tidy = False
        if tidy:
            return "".join(str(x) for x in v2)
                 

    

with open("B-large.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = lines[0]
    for i in range(1, len(lines)):
        N = lines[i].strip()
        ofile.write("Case #{}: {}\n".format(i, solve(N)))
        