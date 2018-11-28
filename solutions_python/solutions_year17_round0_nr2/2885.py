import fileinput

def is_tidy(n):
    while n > 0:
        last = n % 10
        n /= 10
        if last < n % 10:
            return False
        
    return True

def transform(x):
    pown = 1
    while x // (pown * 10) > 0:
        pown *= 10
    powns = pown
    while pown > 1 and is_tidy(x // (pown  / 10)):
        pown /= 10

    return (x // pown - 1) * pown + pown - 1



def main():
    fin = fileinput.input()
    T = int(next(fin))  # number of test cases
    for case in range(1, T + 1):
        n = int(next(fin))
        if is_tidy(n):
            print("Case #{}: {}".format(case, n))
            continue
        # num_dig = int(log(n) / log(10) + 0.1) + 1
        res = n

        add = 0
        counter = 1
        if res % 10 == 1 or res % 10 == 0:
            res /= 10
            while (res % 10 == 1 or res % 10 == 0) and res != 0:
                res /= 10
                add = add * 10 + 9
                counter *= 10
            if res != 0:
                res -= 1
                counter *= 10
                add = add * 10 + 9
            res = res * counter + add

        if is_tidy(res):
            print("Case #{}: {}".format(case, res))
            continue


        while not is_tidy(res):
            res = transform(res)

        print("Case #{}: {}".format(case, res))

if __name__ == '__main__':
    main()