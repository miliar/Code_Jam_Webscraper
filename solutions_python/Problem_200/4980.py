def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())

        while not is_nondecreasing(str(n)):
            n -= 1

        print("Case #{0}: {1}".format(i, n))

def is_nondecreasing(num):
    prevNum = 0
    for i in num:
        if prevNum == 0:
            prevNum = int(i)
            continue
        else:
            if prevNum > int(i):
                return False
            else:
                prevNum = int(i)

    return True

if __name__ == "__main__":
    main()
