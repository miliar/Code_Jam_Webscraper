fileHandle = open('in.txt', 'r')
outputHandle = open('out.txt', 'w')


def gcd(a, b):
    while True:
        if b % a == 0:
            result = a
            break
        b = b % a
        if a % b == 0:
            result = b
            break
        a = a % b

    return result


def lowest_term(a, b):
    _gcd = gcd(a, b)

    return [a/_gcd, b/_gcd]


def gen_result(a, b):
    [a, b] = lowest_term(a, b)

    for i in range(1, 41):
        if a*(2**i) == b:
            return i
        if a*(2**i) > b:
            if a*(2**(40-i)) % b == 0:
                return i
            else:
                break

    return -1


caseNumber = int(fileHandle.readline())

for i in range(caseNumber):
    [a, b] = [int(j) for j in fileHandle.readline().split("/")]
    result = gen_result(a, b)

    if result == -1:
        outputHandle.write("Case #"+str(i+1)+": impossible\n")
    else:
        outputHandle.write("Case #"+str(i+1)+": "+str(result)+"\n")


fileHandle.close()
outputHandle.close()