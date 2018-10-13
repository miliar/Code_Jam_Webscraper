def pattern(string):
    patt = []
    brace = False
    cid = 0
    for ch in string:
        if ch == "(":
            brace = True
            patt.append(str(""))
        elif ch == ")":
            brace = False
            cid += 1
        elif brace == True:
            patt[cid] += ch
        else:
            patt.append(ch)
            cid += 1
    return patt

def match(word, patt):
    for c, t in zip(word, patt):
        if c not in t:
            return False
    return True
        

with open("A.in") as infile:
    with open("A.out",mode="wt") as outfile:
        length, words, cases = [int(x) for x in infile.readline().split()]
        dict = set()
        for nword in range(words):
            dict.add(infile.readline().split()[0])
        print(dict)
        for ncase in range(cases):
            # Perform all nessesary calculation
            patt = pattern(infile.readline().split()[0])
            print(patt)
            num = sum((match(w, patt) for w in dict))
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data=num))
print("Ready")
