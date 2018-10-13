#!/usr/bin/python

def main():
    with open ('A-large.in', 'r') as f, open('A-large.out', 'w') as g:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            a, b = f.readline().split()
            a = int(a.replace('+','0').replace('-','1'), 2)
            b = int(b)
            c = 2**b - 1
            d = 0
            while a >= c:
                if a % 2 == 0:
                    a = a / 2
                else:
                    a = a ^ c
                    d = d + 1
            if a == 0:
                g.write("Case #" + str(i) + ": " + str(d) + "\n")
            else:
                g.write("Case #" + str(i) + ": IMPOSSIBLE\n")



if __name__ == "__main__":
    main()
