def main():
    n = int(raw_input())
    for c in range(1, n + 1):
        plates = int(raw_input())
        pancakes = map(int, raw_input().split())
        res = max(pancakes)
        split = 2
        while split < res:
            res = min(res, sum([(x - 1) // split for x in pancakes]) + split)
            split += 1
        print('Case #%d: %s' % (c , res))
        
if __name__ == "__main__":
    main()    