from collections import Counter

def solve(S):
    c = Counter(S)
    number = []

    for _ in xrange(c["Z"]):
        number.append(0)
        for letter in "ZERO":
            c[letter] -= 1

    for _ in xrange(c["G"]):
        number.append(8)
        for letter in "EIGHT":
            c[letter] -= 1

    for _ in xrange(c["H"]):
        number.append(3)
        for letter in "THREE":
            c[letter] -= 1

    for _ in xrange(c["U"]):
        number.append(4)
        for letter in "FOUR":
            c[letter] -= 1

    for _ in xrange(c["F"]):
        number.append(5)
        for letter in "FIVE":
            c[letter] -= 1

    for _ in xrange(c["W"]):
        number.append(2)
        for letter in "TWO":
            c[letter] -= 1

    for _ in xrange(c["O"]):
        number.append(1)
        for letter in "ONE":
            c[letter] -= 1

    for _ in xrange(c["X"]):
        number.append(6)
        for letter in "SIX":
            c[letter] -= 1

    for _ in xrange(c["S"]):
        number.append(7)
        for letter in "SEVEN":
            c[letter] -= 1

    for _ in xrange(c["I"]):
        number.append(9)
        for letter in "NINE":
            c[letter] -= 1

    return ''.join(map(str, sorted(number)))


def main():
    T = input()
    for N in xrange(T):
        print "Case #{}: {}".format(N + 1, solve(raw_input()))

if __name__ == "__main__":
    main()
