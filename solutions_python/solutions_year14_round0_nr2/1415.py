def main():
    T = int(input())

    for T in range(T):
        C, F, X = (float(x) for x in input().split())
        print("Case #{}: {}".format(T+1, "%.7f" % solve(C, F, X)))
        
def solve(C, F, X):
    farms = 0
    current = 0
    totalCost = X / (2 + farms * F)
    totalIfWait = (X / (2 + (farms + 1) * F)) + C / (2 + farms * F)

    while (totalCost > totalIfWait):
        current += C / (2 + farms * F)
        farms += 1

        totalCost = X / (2 + farms * F)
        totalIfWait = (X / (2 + (farms + 1) * F)) + C / (2 + farms * F)        

    return current + X / (2 + farms * F)
    
if __name__ == '__main__':
    main()
