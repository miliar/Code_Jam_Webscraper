def to_base(num, base):
    converted_num = ''

    while num > 0:
        converted_num = str(num % base) + converted_num
        num /= base

    return converted_num

def is_happy(num, base):

    num = to_base(num, base)

    sums = [num, ]
    while(True):
        sum = 0
        for digit in sums[-1]:
            sum += int(digit) * int(digit)
        sum = to_base(sum, base)

        if sum == str(1):
            return True
        if sum in sums:
            return False

        sums.append(sum)

def lowest_happy(bases):
    i = 2

    while True:
        all_happy = True
        for base in bases:
            if not is_happy(i, base):
                all_happy = False
                break
        if all_happy:
            break
        i += 1

    return i


INPUT = open('A-small-attempt0.in')
OUTPUT = open('A-small-attempt0.out', 'w')

T = int(INPUT.readline().strip())

for i in range(T):
    print (str(i + 1) + "/" + str(T))
    bases = INPUT.readline().split()
    for j in range(len(bases)):
        bases[j] = int(bases[j])

    print >> OUTPUT, "Case #" + str(i + 1) + ": " + str(lowest_happy(bases))

INPUT.close()
OUTPUT.close()
