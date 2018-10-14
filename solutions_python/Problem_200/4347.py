import sys

t = int(raw_input())

numbers = list()

for i in range(t):
    numbers.append(int(raw_input()))

output_file = "solution.out"
with open(output_file, 'w') as dsout:
    for x in range(t):
        number = numbers[x]
        digits = list()
        while number > 0:
            digits.append(number % 10)
            number = number/10
        dlen = len(digits)-1
        digits = digits[::-1]
        if all(x == 9 for x in digits):
            pass
        elif all(x <= y for x, y in zip(digits, digits[1:])):
            print 'incr'
            pass
        else:
            for j in range(dlen):
                pref = []
                if digits[j] > digits[j+1]:
                    digits[j] -= 1
                    pref = digits[:j+1]
                    suf = [9] * (dlen - j)
                    digits = pref
                    digits.extend(suf)
                    break
                elif digits[j] == digits[j+1]:
                    pref = digits[:j+1]
                    pref = map(lambda h: 0 if h==0 else h-1, pref)
                    suf = [9] * (dlen - j)
                    digits = pref
                    digits.extend(suf)
                    break

        digits = map(str, digits)
        print "Current " + str(numbers[x]) + ' = ' + str(int(''.join(digits)))
        dsout.write("Case #{}: {}\n".format(1+x, int(''.join(digits))))
