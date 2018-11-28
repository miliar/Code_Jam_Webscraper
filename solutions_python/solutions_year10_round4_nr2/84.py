import math
def find_price(M):
    p = math.log(len(M), 2)
    prices = [p - i for i in M]

    price = 0
    while p:
        prices_t = [max([prices[i], prices[i+1]]) for i in range(0, len(prices), 2)]
        for i in range(len(prices_t)):
            if prices_t[i] == p:
                prices_t[i] -= 1
                price += 1
        p -= 1
        prices = prices_t

    return int(prices[0] + price)
    
def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    T = int(lines[0])
    cnt = 1
    R = []
    for i in range(T):
        try:
            P = int(lines[cnt])
            M = map(int, lines[cnt + 1].split())
            
            R.append("Case #%d: %d" % (i + 1, find_price(M)))
            cnt += 2 + P
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))
