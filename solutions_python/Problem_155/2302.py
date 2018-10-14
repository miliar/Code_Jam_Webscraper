import sys
import re


def solve(m, s):
    total = 0
    add = 0
    for i in range(int(m)+1):
        d = int(s[i])
        if total < i:
            add += i-total
            total += i-total
        total += d
    return str(add)


def main():
    f = open('A-large.in', 'r')
    output = open('A-large.out', 'w')
    text = f.read()
    f.close()
    lines = re.split("[\n|\r]",text)
    T = int(lines[0])
    
    for n in range(1,T+1):
        m, s = lines[n].split(' ')
        ans = solve(m, s)
        output.write('Case #' + str(n) + ': ' + ans + '\n')
            
    output.close()

    

if __name__ == '__main__':
    main()
