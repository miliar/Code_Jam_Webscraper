import sys

dict = {
    "1": {"1": "1", "i": "i", "j": "j", "k": "k"},
    "i": {"1": "i", "i": "-1", "j": "k", "k": "-j"},
    "j": {"1": "j", "i": "-k", "j": "-1", "k": "i"},
    "k": {"1": "k", "i": "j", "j": "-i", "k": "-1"}
}

fd = open("./C-small.in", "r")

fout = open("./C-small.out", "w")

num_tests = int(fd.readline().strip())

fulldict = {}

def checkIJK(string):
    res = string[0]
    for j in range(1, len(string)):
        if res == "i":
            res2 = string[len(string) - 1]
            for k in reversed(range(len(string) - 1)):
                if k < j:
                    return "NO"

                if res2 == "k":
                    res3 = string[j]
                    for l in range(j + 1, k + 1):
                        res3 = fulldict[(res3, string[l])]

                    if res3 == "j":
                        return "YES"

                res2 = fulldict[(string[k], res2)]

        res = fulldict[(res, string[j])]

    return "NO"



for i, d in dict.items():
    for j, res in d.items():
        fulldict[(i, j)] = res
        fulldict[("-" + i, "-" + j)] = res

        if res[0] == '-':
            fulldict[("-" + i, j)] = res.replace("-", "")
            fulldict[(i, "-" + j)] = res.replace("-", "")
        else:
            fulldict[("-" + i, j)] = "-" + res
            fulldict[(i, "-" + j)] = "-" + res

print(fulldict)
for i in range(num_tests):
    test = fd.readline().strip().split(" ")

    L = int(test[0])
    X = int(test[1])

    string = fd.readline().strip() * X
    print(string)

    res = string[0]
    found_i = False
    for j in range(1, len(string)):
        if res == "i":
            found_i = True
        res = fulldict[(res, string[j])]

    if res == "-1":
        result = "YES"
    else:
        result = "NO"

    if len(string) <= 3 and string != "ijk":
        result = "NO"

    if string.count("i") == len(string) or string.count("j") == len(string) or string.count("k") == len(string):
        result = "NO"

    if not found_i:
        result = "NO"



    if result == "YES":
        result = checkIJK(string)

    fout.write("Case #{}: {}".format(i + 1, result) + "\n")
    print("Case #{}: {}".format(i + 1, result))


fout.close()
fd.close()

