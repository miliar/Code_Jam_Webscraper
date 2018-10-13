import sys
import re



def solve(n):
##    s = n[0]*len(n)
##    if n == s:
##        return n
##    if n < s:
##        if s[0] == "1":
##            return "9"*(len(n)-1)
##        else:
##            return str(int(s[0])-1) + "9"*(len(n)-1)
##    return "ERR"
    pc = "0"
    for i,c in enumerate(n):
        if c < pc:
            c = pc
            i -= 1
            break
        pc = c
    if i == len(n)-1:
        return n
    while i > 0:
        if n[i] <> n[i-1]:
            break
        i -= 1
    ns = ""
    for j,c in enumerate(n):
        if j == i:
            ns += str(int(c)-1)
            break
        ns += c
    ns = ns + "9"*(len(n)-len(ns))
    if ns[0] == "0":
        return ns[1:]
    return ns


def main():
    f = open('B-large.in', 'r')
    output = open('B-large.out', 'w')
    text = f.read()
    f.close()
    lines = re.split("[\n|\r]",text)
    T = int(lines[0])

    n = 1
    for line in lines[1:T+1]:
        ans = solve(line)
        output.write('Case #' + str(n) + ': ' + ans + '\n')
        n += 1
            
    output.close()

    

if __name__ == '__main__':
    main()
