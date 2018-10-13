def is_tidy(num):
    return int(''.join(sorted(str(num)))) == num

def naive_tidify(num):
    while True:
        if is_tidy(num):
            return num
        num -= 1

def tidify(num):
    digits = list(map(int, str(num)))
    max_left = 0
    for index, digit in enumerate(digits):
        max_left = max(max_left, digit)
        if digit >= max_left:
            continue
        pivot = digits.index(max(digits[:index]))
        digits[pivot] -= 1
        for i in range(pivot+1, len(digits)):
            digits[i] = 9
        break
    return int(''.join(map(str, digits)))

dataset_file = 'B-large.in'
dataset = []
with open(dataset_file) as tests:
    tests.readline()
    for line in tests:
        dataset.append(int(line.strip()))

with open('out.txt', 'w') as out:
    for i, n in enumerate(dataset):
        out.write(f"Case #{i+1}: {tidify(n)}\n")
    