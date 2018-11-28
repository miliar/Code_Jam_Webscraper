def read_input():
    line = input()
    # print(line)
    length = len(line)
    # print(length)
    value = int(line)
    # print(value)
    digits = [0]*length
    for i in range(0, length):
        digits[i] = (value // (10**i)) % 10
    # print(digits)
    for i in range(0, length):
        if i==length-1:
            break
        if digits[i] < digits[i+1]:
            digits[i+1] -= 1
            for j in range(0, i+1):
                digits[j] = 9
        # print(digits)
    return sum([digits[i] * 10**i for i in range(0, length)])

numCases = int(input())
# print(numCases)
for i in range(1, numCases + 1):
    output = read_input()
    print("Case #%d:" % i, output)
