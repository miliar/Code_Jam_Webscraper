

def unicorn(total, u):
    for uniTup in u:
        if uniTup[0] > (total / 2):
            return "IMPOSSIBLE"
    u = sorted(u, reverse = True)
    num, col = u[0][0], u[0][1]
    s = col
    num -= 1
    u.pop(0)
    u.append((num, col))
    while len(s) < total:
        u = sorted(u, reverse = True)
        if u[0][1] != s[-1]:
            num, col = u[0][0], u[0][1]
            s += col
            num -= 1
            u.pop(0)
            u.append((num, col))
        else:
            num, col = u[1][0], u[1][1]
            s += col
            num -= 1
            u.pop(1)
            u.append((num, col))
    if s[0] == s[-1]:
        s = s[:-2] + s[-1] + s[-2]
    return s





if __name__ == '__main__':
    inputName = "smallUnicorn.txt"
    outputName = "outputSmallUnicorn.txt"
    f = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/Round 2A/" + inputName,'r')
    w = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/Round 2A/" + outputName,'w')
    cases = int(f.readline())
    c = 1
    while cases > 0:
        line = f.readline().split()
        total = int(line[0])
        w.write("Case #" + str(c) + ": " + unicorn(total, [ (int(line[1]), "R"), (int(line[2]), "O"), (int(line[3]), "Y"), (int(line[4]), "G"), (int(line[5]), "B"), (int(line[6]), "B")  ]) + "\n")
        cases -= 1
        c += 1
    f.close()
    w.close()
    # print(unicorn(542, [(55, "R"), (0, "O",), (234, "Y"), (0, "G"), (253, "B"), (0, "V")] ) )
    # 542 55 0 234 0 253 0




# def removeCharFromStr(str, index):
#     endIndex = index if index == len(str) else index + 1
#     return str[:index] + str[endIndex:]
#
# # 'ab' -> a + 'b', b + 'a'
# # 'abc' ->  a + bc, b + ac, c + ab
# #           a + cb, b + ca, c + ba
# def perm(str):
#     if len(str) <= 1:
#         return {str}
#     permSet = set()
#     for i, c in enumerate(str):
#         newStr = removeCharFromStr(str, i)
#         retSet = perm(newStr)
#         for elem in retSet:
#             if isValid(c+elem): return c + elem
#             permSet.add(c + elem)
#     return permSet

#
# from itertools import permutations
# from random import shuffle
#
# def getString(u):
#     answer = ""
#     answer += u[0] * "R"
#     answer += u[1] * "O"
#     answer += u[2] * "Y"
#     answer += u[3] * "G"
#     answer += u[4] * "B"
#     answer += u[5] * "V"
#     answer = list(answer)
#     shuffle(answer)
#     return "".join(answer)
#
# def isValid(s):
#     if s[0] == s[len(s) - 1]: return False
#     else:
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]: return False
#     return True
#
#
# def unicorn(total, u):
#     for uni in u:
#         if uni > (total / 2):
#             return "IMPOSSIBLE"
#     s = getString(u)
#     for p in permutations(s):
#         print(p)
#         please = "".join(p)
#         if isValid(please):
#             return please
