debug = False
prev_digit = ['0','0','1','2','3','4','5','6','7','8']

def dbg_print(x):
    if debug:
        print(x)

def tidy(n):
    l = len(n)
    for i in range(1, l):
        if n[i] < n[i-1]:
            return False
    return True

def reduce(n):
    l = len(n)
    for i in range(1, l):
        if n[i] < n[i-1]:
            n[i-1] = prev_digit[int(n[i-1])]
            for j in range(i, l):
                n[j] = '9'
            return n
    print("Reduce didn't make any change ?!")
    return n

def remove_leading_zeroes(n):
    i = 0
    while n[i] == '0':
        i = i + 1
    return n[i:]

def main():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = input() # read 1 integer as a string
        n = list(n)

        dbg_print(n)
        while not tidy(n):
            n = reduce(n)
            dbg_print(n)

        n = remove_leading_zeroes(n)
        n = ''.join(n)

        print("Case #{}: {}".format(i, n))

if __name__ == "__main__":
    main()
