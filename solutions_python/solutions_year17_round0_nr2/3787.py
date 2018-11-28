import sys


def max_tidy(n):
    chars = list(str(n))

    while True:
        for i in range(1, len(chars)):
            if chars[i] >= chars[i-1]:
                continue
            else:
                split = i
                break
        else:
            return int(''.join(chars))

        left = list(str(int(''.join(chars[:split])) - 1))
        right = ['9'] * len(chars[split:])
        chars = left+right

def main():
    t = int(sys.stdin.readline())   

    for case in range(1, t+1):
        n = int(sys.stdin.readline())
        print "Case #{}: {}".format(case, max_tidy(n))
        

if __name__ == "__main__":
    main()

