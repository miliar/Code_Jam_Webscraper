#! /usr/bin/python3

def main():
    T = int(input())
    for i in range(1, T + 1):
        n, s = input().split()
        need = 0
        standing = 0
        shyness = map(int, s)
        for x, y in enumerate(shyness):
            if x > standing:
                need += x - standing
                standing += y + x - standing
            else:
                standing += y
        print("Case #%d: %d" % (i, need))

if (__name__ == "__main__"):
    main()
