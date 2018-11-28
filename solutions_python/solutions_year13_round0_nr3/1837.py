

def fairAndSquares(a, b):
    fairAndSquare = []
    for i in range(a, b + 1):
        if isPalindrome(i) and hasPalindromeSqrt(i):
            fairAndSquare.append(i)
    return fairAndSquare

def isPalindrome(num):
    rev = 0
    tmp = num
    while 0 < tmp:
        rev *= 10
        rev += tmp % 10
        tmp = int(tmp / 10)
    return num == rev

def hasPalindromeSqrt(n):
    sqr = n ** (0.5)
    if 0 == sqr - int(sqr):
        return isPalindrome(int(sqr))
    return False



def jamout(filename, outputs):
    fout = open(filename, 'wt')
    for i, output in enumerate(outputs):
        fout.write('Case #' + str(i + 1) + ': ' + output + "\n")
    fout.close()



filename = 'C-small-attempt0.in'
datasets = []
with open(filename) as f:
    testCases = int(next(f))
    while 0 < testCases:
        datasets.append([int(e) for e in next(f).rstrip().split()])
        testCases -= 1

outputs = []
for dataset in datasets:
    outputs.append(str(len(fairAndSquares(dataset[0], dataset[1]))))

jamout('C-small-attempt0.txt', outputs)
    
