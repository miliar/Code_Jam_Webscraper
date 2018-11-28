def main():
    with open('input') as f:
        cases = int(f.readline()[:-1])
        for casen in range(cases):
            case = f.readline()[:-1]
            res = ''
            for s in case:
                if not res:
                    res += s
                elif s < res[0]:
                    res += s
                else:
                    res = s + res

            print("Case #{0}: {1}".format(casen + 1, res))


if __name__ == '__main__':
    main()