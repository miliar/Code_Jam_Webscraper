def isneat(n):
    x = 10
    while n:
        if x< n%10:
            return False
        x = n%10
        n = n//10
    return True

def main():
    f = open("answer.txt", "w")
    tests = open("B-small-attempt0.in").read().splitlines()
    i = 1
    for line in tests[1:]:
        s = int(line)
        while not isneat(s):
            s-=1

        ans = s
        print(f"Case #{i}: {ans}", file=f)
        i+=1

main()