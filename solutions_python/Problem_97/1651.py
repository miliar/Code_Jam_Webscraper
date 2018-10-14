def switch(number, n):
    """ Switch the digits of number n time """
    for _ in range(n):
        number = (number*10)%(10**len(str(number))) + number/(10**(len(str(number))-1))
    return number


def test(A, B):
    pairs = []
    for number in range(A, B+1):
        for i in range(1, len(str(number))):
            n, s = number, switch(number, i)
            if not n == s and A <= s <= B and not (n, s) in pairs and not (s,n) in pairs:
                pairs.append((n,s))
    return len(pairs)

if __name__ == "__main__":
    for i in range(int(raw_input())):
        line = [int(c) for c in raw_input().split()]
        print("Case #{}: {}".format(i+1, test(line[0], line[1])))
