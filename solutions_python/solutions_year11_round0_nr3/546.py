
import itertools

def sum(a):
    sum = 0
    for b in a:
        sum += b
    return sum

def brokenSum(a):
    sum = 0
    for b in a:
        sum ^= b
    return sum

if __name__ == '__main__':
    inFile = open('C-small-attempt1.in', 'r')
    outFile = open('C-small-attempt1.out', 'w')
    numCases = int(inFile.readline())
    print("Cases:", numCases)
    for case in range(numCases):
        outFile.write('Case #{0}: '.format(case + 1))

        inFile.readline() # discard
        
        candy = inFile.readline().rsplit()
        for c in range(len(candy)):
            candy[c] = int(candy[c])
        print(candy)
        a = brokenSum(candy)
        if a != 0:
            result = 'NO'
        else:
            m = 0
            for bb in range(len(candy) // 2):
                for i in itertools.combinations(candy, bb + 1):
                    ii = itertools.filterfalse(lambda x: x in i, candy)
                    if brokenSum(i) ^ a == brokenSum(i):
                         m = max((m, sum(i), sum(ii)))
            if m == 0:
                result = 'NO'
            else:
                result = m
                    
        print('result:', result)
        outFile.write(str(result) + '\n')
    outFile.close()
    inFile.close()
