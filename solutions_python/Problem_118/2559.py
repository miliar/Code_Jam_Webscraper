import math

def is_pal(n):
    s = str(n)
    return s == s[::-1]
    
def check(a, b):
    num = 0;
    for i in range(a, b + 1):
        if not is_pal(i):
            continue
        r = math.sqrt(i)
        if r != int(r):
            continue
        if not is_pal(int(r)):
            continue
        num = num  + 1
    return num

def main():
    file = open("./C-small-attempt0.in", "r")
    line = file.read()
    lines = line.splitlines()
    T = int(lines[0])
    for i in range(T):
        [a, b] = map(int, lines[i+1].split())
        print "Case #{0}: {1}".format(i + 1, check(a, b))
        
if __name__ == "__main__":
    main()