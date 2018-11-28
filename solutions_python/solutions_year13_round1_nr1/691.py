
import sys

def calculate(r, t):
    result = 0
    radius = r

    while (True):
        A = (radius + 1)**2 - radius**2
        if A <= t:
            t = t - A
            result = result + 1
            radius = radius + 2 
        else:
            break

    return result
        

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        L = sys.stdin.readline().strip()
        if L == "":
            break
        L = L.split()
        (r, t) = map(int, L)
        print ("Case #{0}: {1}".format(i + 1, calculate(r, t)))

    pass


if __name__ == "__main__":
    main()


