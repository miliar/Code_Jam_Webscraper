def main():
    tests = int(raw_input())
    for test in xrange(tests):
        c, f, x = map(float, raw_input().split())
        oldbest = x + 1
        rate = 2.0
        best = x/rate
        runtime = 0.0
        while best < oldbest:
            oldbest = best
            runtime += c/rate
            rate += f
            best = x/rate + runtime
        output = "Case #{0}: {1:.7f}".format(test + 1, oldbest)
        print(output)

if __name__ == "__main__":
    main()
