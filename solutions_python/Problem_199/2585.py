from math import ceil, floor, log, log2
def solve(pan, k):
    pan = trans(pan)
    k = int(k)
    i = 0
    flips = 0
    while i < len(pan):
        current = pan[i]
        if current:
            i += 1
            continue
        if len(pan) - i < k:
            return False
        
        flip(pan, i, i+k)
        flips += 1
    
    
    return flips

def flip(arr, start, end):
    for i in range(start, end):
        arr[i] = not arr[i]

def trans(pans):
    return [True if pan == "+" else False for pan in pans]

def main():
    inputs = int(input())
    res = []
    for _ in range(inputs):
        res.append(solve(*input().split(" ")))

    for i, sol in enumerate(res):
        print("Case #%d: %s" % (i+1, sol if sol is not False else "IMPOSSIBLE"))


if __name__ == "__main__":
    main()

