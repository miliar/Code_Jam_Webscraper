def isTidy(number):
    temp = str(number)
    size = len(temp)
    for i in range(size-1, 0, -1):
        if int(temp[i]) < int(temp[i-1]):
            return False
    return True

def makeTidy(number):
    temp = str(number)
    size = len(temp)
    if size < 2:
        return number
    else:
        if isTidy(number) is True:
            return number
        for i in range(1, size):
            if int(temp[i-1]) > int(temp[i]):
                return makeTidy(int(temp)-(int(temp[i:])+1))

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        print("Case #{}: {}".format(i, makeTidy(n)))

if __name__ == "__main__":
    main()

