import sys
fp = open('input_large')
case_num = int(fp.readline())
for i in range(case_num):
    numbers = sorted([int(x) for x in fp.readline().split()][1:])
    subs = []
    for j in range(1, len(numbers)):
        subs.append(numbers[j] - numbers[j - 1])
    import fractions
    gcd = reduce(fractions.gcd, subs)
    if numbers[0] % gcd == 0:
        answer = 0
    else:
        answer = gcd - numbers[0] % gcd;
    print "Case #%d: %d" % (i + 1, answer)
