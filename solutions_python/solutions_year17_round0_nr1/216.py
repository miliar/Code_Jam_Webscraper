# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

f = open("A-large.in",'r')
g = open("Answer.txt", 'w')


t = int(f.readline())  # read a line with a single integer
for i in range(1, t + 1):
    s, k = f.readline().strip().split(" ")
    k = int(k)
    print i, s, k
    if k > len(s):
        g.write("Case #{}: {}\n".format(i, "IMPOSSIBLE") )
        continue
    count = 0
    for j in range(len(s) - k + 1):
        if s[j] == "-":
            count += 1
            sub = ""
            for l in range(j, j+k):
                sub = sub + "-" if s[l] == "+" else sub + "+"
            s = s[:j] + sub + s[j+k:]
            print s, count
    for j in range(len(s)-k, len(s)):
        if s[j] == "-":
            count = "IMPOSSIBLE"
            break
    g.write("Case #{}: {}\n".format(i, count) )
#end_for
