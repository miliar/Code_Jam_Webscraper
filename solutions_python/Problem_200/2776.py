def solve(number):
    if is_tidy(number):
        return number
    return int(str(solve(number//10 - 1)) + "9")     

def is_tidy(number):
    idigits = list(map(int, str(number)))
    return sorted(idigits) == idigits

def main():
    inputs = int(input())
    res = []
    for _ in range(inputs):
        res.append(solve(int(input())))

    for i, sol in enumerate(res):
        print("Case #%d: %d" % (i+1, sol))


if __name__ == "__main__":
    main()
