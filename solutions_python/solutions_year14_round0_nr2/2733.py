import sys

def main():
    with open(sys.argv[1]) as inp:
        cases = int(inp.readline())
        for case in range(1, cases + 1):
            c, f, x = map(float, inp.readline().split())
            rate = 2.0
            cookies = 0
            res = 0
            while True:
                cost_to_buy = c / rate + x / (rate + f)
                cost_not_to_buy = x / rate
                if cost_not_to_buy < cost_to_buy:
                    res += cost_not_to_buy
                    break
                else:
                    res += c / rate
                    rate += f
            print "Case #{}: {}".format(case, res)


if __name__ == "__main__":
    main()
