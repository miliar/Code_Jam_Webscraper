import sys

matr = dict()
matr["11"] = "1"
matr["1i"] = "i"
matr["1j"] = "j"
matr["1k"] = "k"
matr["i1"] = "i"
matr["ii"] = "-1"
matr["ij"] = "k"
matr["ik"] = "-j"
matr["j1"] = "j"
matr["ji"] = "-k"
matr["jj"] = "-1"
matr["jk"] = "i"
matr["k1"] = "k"
matr["ki"] = "j"
matr["kj"] = "-i"
matr["kk"] = "-1"

matr["-11"] = "-1"
matr["-1i"] = "-i"
matr["-1j"] = "-j"
matr["-1k"] = "-k"
matr["-i1"] = "-i"
matr["-ii"] = "1"
matr["-ij"] = "-k"
matr["-ik"] = "j"
matr["-j1"] = "-j"
matr["-ji"] = "k"
matr["-jj"] = "1"
matr["-jk"] = "-i"
matr["-k1"] = "-k"
matr["-ki"] = "-j"
matr["-kj"] = "i"
matr["-kk"] = "1"

matr["-1-1"] = "1"
matr["-1-i"] = "i"
matr["-1-j"] = "j"
matr["-1-k"] = "k"
matr["-i-1"] = "i"
matr["-i-i"] = "-1"
matr["-i-j"] = "k"
matr["-i-k"] = "-j"
matr["-j-1"] = "j"
matr["-j-i"] = "-k"
matr["-j-j"] = "-1"
matr["-j-k"] = "i"
matr["-k-1"] = "k"
matr["-k-i"] = "j"
matr["-k-j"] = "-i"
matr["-k-k"] = "-1"

matr["1-1"] = "-1"
matr["1-i"] = "-i"
matr["1-j"] = "-j"
matr["1-k"] = "-k"
matr["i-1"] = "-i"
matr["i-i"] = "1"
matr["i-j"] = "-k"
matr["i-k"] = "j"
matr["j-1"] = "-j"
matr["j-i"] = "k"
matr["j-j"] = "1"
matr["j-k"] = "-i"
matr["k-1"] = "-k"
matr["k-i"] = "-j"
matr["k-j"] = "i"
matr["k-k"] = "1"

def multi(a, b):
    return matr[a + b]

def evaluate(substr):
    res = "1"
    for i in substr:
        res = multi(res, i)

    return res

def find_ijk(substr):
    searching_for = "i"
    res = "1"
    for i in substr:
        res = multi(res, i)
        if res == searching_for:
            if searching_for == "i":
                searching_for = "j"
                res = "1"
            elif searching_for == "j":
                searching_for = "k"
                res = "1"
    if searching_for == "k" and res == "k":
        return True
    else:
        return False

in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for i in range(t):
    params = in_file.readline().split(' ')
    l = int(params[0])
    x = int(params[1])

    lx = in_file.readline().strip()
    ans = "YES"
    if evaluate(lx) == "1":
        ans = "NO"

    min_x = float("inf")
    step = 1
    test = lx
    while evaluate(test) != "-1" and step < 5:
        test += lx
        step += 1

    if evaluate(test) == "-1":
        min_x = step

    if min_x > x:
        ans = "NO"

    if evaluate(lx) != "-1" and (x - min_x) % 4 != 0:
        ans = "NO"


    if evaluate(lx) == "-1" and (x - min_x) % 2 != 0:
        ans = "NO"

    if ans == "YES":
        expansion = min(12, x - min_x)
        for j in range(expansion):
            test += lx
        ans = "NO"
        if find_ijk(test):
            ans = "YES"

    out_file.write("Case #" + str(i + 1) + ": " + ans)

    out_file.write("\n")

in_file.close()
out_file.close()
