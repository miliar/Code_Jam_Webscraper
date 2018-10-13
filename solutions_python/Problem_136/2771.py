def solve():
    elapsed = 0.0
    Rate = 2.0
    Candy = X

    while True:
        JustDoIt = Candy/Rate
        BuyFarm = (Candy)/(Rate+F)
        BuyTime = float(C)/Rate

        if JustDoIt < BuyFarm+BuyTime:
            return elapsed+JustDoIt
        elapsed += BuyTime
        Rate += F

for idx in range(1, input()+1):
    C, F, X = map(float, raw_input().strip().split())
    print('Case #%d: %.7f' % (idx, solve()))
