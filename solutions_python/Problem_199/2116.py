def solution():
    s, k = input().split(" ")
    s = list(s)
    k = int(k)
    flips = 0

    for i in range( len(s) - k + 1 ):
        
        if( s[i] == "-" ):
            flips += 1
            for j in range(k):
                s[i+j] = "+" if (s[i+j] == "-") else "-"

    if("-" in s):
        return "IMPOSSIBLE"

    else:
        return flips

testcases = int(input())
for i in range(testcases):
    print("Case #" + str(i+1) + ": " + str(solution()))
