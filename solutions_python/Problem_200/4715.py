def is_tidy(n):
    s = str(n)

    prev = 0
    for c in s:
        i = int(c)
        if i >= prev:
            prev = i
        else:
            return False
    return True

def prev_tidy(n):
    for i in range(n, 0, -1):
        if is_tidy(i):
            return i

def main():
    # read a line with a single integer
    t = int(input())
    for i in range(1, t + 1):
        # read a list of integers, 2 in this case
        n = int(input())
        answer = prev_tidy(n)
        print("Case #{}: {}".format(i, answer))

if __name__ == '__main__':
    main()
