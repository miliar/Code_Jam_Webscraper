import string

f = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq"
t = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz"
table = string.maketrans(f, t)

inp = open("t.in")
size = int(inp.readline())

for test in range(1, size + 1):
    line = inp.readline().strip()
    temp = "Case #" + str(test) + ": " + string.translate(line, table)
    print(temp)

"""
ejpmysljylckdkxveddknmcrejsicpdrysi




lines = inp.readlines()
for line in lines:
    temp = line.strip().replace(" ", "")
    print(temp)

a = "abcda"
b = "qwerq"
table = string.maketrans(a, b)
s = string.translate("abcdabcda", table)
print(s)
"""
