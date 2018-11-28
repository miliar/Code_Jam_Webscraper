import sys

def tidy(n):
    str_n = str(n)
    list_str_n = list(str_n)
    l = len(str_n)
    i = 1;
    while i < l:
        if int(list_str_n[i]) < int(list_str_n[i-1]):
            j = i
            while j < l:
                list_str_n[j]= '9'
                j +=1
            list_str_n[i-1] = str(int(list_str_n[i-1])-1)
            return int(''.join(list_str_n))
        i += 1
    return int(''.join(list_str_n))

name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    n = int(raw_input())
    while(n != tidy(n)):
        n = tidy(n)
    print("Case #" + str(testCase) + ": " + str(n))