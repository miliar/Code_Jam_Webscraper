# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

f = open("B-large.in",'r')
g = open("Answer.txt", 'w')

def solve(s):
    if len(s) < 1: return s
    if s[0] == "0": return solve(s[1:])
    j = 1
    while j < len(s):
        if s[j] == s[0]:
            j += 1
        else:
             break
        #end_if
    if j == len(s): return s
    if s[0] < s[j]:
        return s[:j] + solve(s[j:])
    else:
        result = "" if s[0] == "1" else str(int(s[0]) - 1)
        for k in range(len(s) - 1): result += "9"
        return result
#end_def

t = int(f.readline())  # read a line with a single integer
for i in range(1, t + 1):
    N = f.readline().strip()
    g.write("Case #{}: {}\n".format(i, solve(N)))
#end_for
