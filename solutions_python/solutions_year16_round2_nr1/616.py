#!/usr/bin/env python3

def parse():
    s = input()
    return s

def solve(s):
    d0 = s.count('Z')
    d2 = s.count('W')
    d4 = s.count('U')
    d6 = s.count('X')
    d8 = s.count('G')
    d5 = s.count('F') - d4
    d7 = s.count('V') - d5
    d1 = s.count('O') - d0 - d2 - d4
    d9 = s.count('I') - d5 - d6 - d8
    d3 = s.count('H') - d8
    return '0'*d0 +'1'*d1+'2'*d2+'3'*d3+'4'*d4+'5'*d5+'6'*d6+'7'*d7+'8'*d8+'9'*d9

def main():
    for i in range(int(input())):
        s = parse()
        d = solve(s)
        print("Case #{}: {}".format(i+1, d))

if __name__ == "__main__": main()
