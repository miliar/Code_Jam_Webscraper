def decrement_number(digits, i):
    for j in range(i+1, len(digits)):
        digits[j] = 9
    if digits[i] != 0:
        digits[i] -= 1
    elif i != 0:
        digits[i] = 9
        digits[i-1] -= 1
    return digits

puzzle = open('question_big.txt').readlines()[1:]

with open('answer_big.txt', 'w') as outfile:
    for i, line in enumerate(puzzle):
        digits = [int(d) for d in list(line.strip())]
        while digits != sorted(list(digits)):
            for j in reversed(range(len(digits)-1)):
                if int(digits[j]) > int(digits[j+1]):
                    digits = decrement_number(digits, j+1)
        outfile.write('Case #%d: %d\n' % (i+1, 
            int(''.join(str(d) for d in digits), 10)))