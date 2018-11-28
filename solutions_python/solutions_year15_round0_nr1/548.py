import sys

def solve(fin):
    m, s = fin.readline().split()
    f = sm = 0
    for i in range(len(s)):
        f += max(0, i - sm - f)
        sm += int(s[i])
    print(f)

def main():
    fin = open("input.txt", "r")
    T = int(fin.readline())
    for _T in range(1, T + 1):
        print("Case #", _T, ": ", sep = "", end = "")
        solve(fin)
    fin.close()

main()