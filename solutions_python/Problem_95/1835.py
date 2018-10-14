with open("a-small.in", "r") as fin:
    with open("a-small.out", "w") as fout:
        en = list("abcdefghijklmnopqrstuvwxyz")
        go = list("ynficwlbkuomxsevzpdrjgthaq") # b, q, z
        m = {}
        for i in range(len(en)):
            m[go[i]] = en[i]
        n = int(fin.readline())
        for case in range(1, n + 1):
            input = fin.readline()
            output = ""
            for c in input:
                if c in m:
                    output += m[c]
                else:
                    output += c
            fout.write("Case #" + str(case) + ": " + output)
