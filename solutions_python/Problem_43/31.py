def to_str(n):
    if n < 10:
        return str(n)
    return chr(ord('a') + n - 10)

def smallest_number(s):
    if len(s) == 1:
        return 1
    known = {}
    largest = 0
    first = s[0]
    known[first] = "1"
    res = "1"
    for symbol in s[1:]:
        if symbol in known:
            res += known[symbol]
        else:
            known[symbol] = to_str(largest)
            largest += 1
            if largest == 1:
                largest = 2
            res += known[symbol]
    base = largest
    if base == 0:
        base = 2
    return int(res, base)

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
        ans = smallest_number(raw_input())
        print "Case #%d: %d" % (i, ans)

if __name__ == "__main__":
    main()
    
