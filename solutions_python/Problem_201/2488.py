def lol(n, k):
    if k >= n:
        return 0, 0

    places = [n]

    for x in xrange(k):
        n = max(places)

        mn = ((n - 1) / 2)
        mx = n - 1 - mn

        if mn:
            places.append(mn)
        if mx:
            places.append(mx)

        places.remove(n)

    return mx, mn


def main():
    t = int(raw_input())
    for i in xrange(t):
        print "Case #{}: {}".format(i + 1, (' '.join(map(str, lol(*map(int, raw_input().split()))))))


if __name__ == "__main__":
    main()
