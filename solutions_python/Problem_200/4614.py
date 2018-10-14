def p(n):
    while True:
        l = list(str(n))
        llen = len(l)
        a = all(l[i] <= l[i+1] for i in range(llen-1))
        if a:
            return n
        else:
            n -= 1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    j = int(input())
    result = p(j)
    print("Case #{}: {}".format(i, result))


"""
def main():
    print(p(132))
    print(p(1000))
    print(p(987))

    print(p(7))
    #print(p(111111111111111110))



main()"""