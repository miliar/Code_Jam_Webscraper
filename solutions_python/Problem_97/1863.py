import sys, string
inputTxt = sys.stdin.readlines()

for i, line in enumerate(inputTxt[1:]):
    pairs = set()
    A, B = map(int, line.split())

    for j in range(A, B):
        digits = str(j)
        #print('digits ', digits)
        for split in range(1, len(digits)):
            if digits[split] != '0':
                n = int(digits[:split]+ digits[split:])
                m = int(digits[split:]+ digits[:split])
                if A <= n < m <= B:
                    #print('j, (n, m) ',j, (n, m))
                    pairs.add((n, m))


    #print(pairs)
    print("Case #{}: {}".format(i+1, len(pairs)))
