def main():
    nCases = int(input())
    for case in range(1, nCases + 1):
        farmCost, boost, target = [float(n) for n in input().split()]
        bestTime = target / 2
        origTime = bestTime
        if farmCost > target:
            print('Case #{}: {}'.format(case, bestTime))
            continue

        currentRate = 2
        currentTime = 0
        while currentTime < origTime:
            timeToBuy = farmCost / currentRate
            currentTime = currentTime + timeToBuy
            currentRate = currentRate + boost
            predicted = currentTime + (target / currentRate)
            if predicted < bestTime:
                bestTime = predicted
            else:
                break

        print('Case #{}: {}'.format(case, bestTime))


if __name__ == "__main__":
    main()
