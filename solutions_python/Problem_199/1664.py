input_file = open('/Users/eunice.lin/Downloads/A-large.in', 'r')

def flip(pancakes, x, k):
    for i in range(x, x+k):
        pancake = pancakes[i]
        if pancake == '+':
            pancakes[i] = '-'
        elif pancake == '-':
            pancakes[i] = '+'

def happy(pancakes):
    for pancake in pancakes:
        if pancake != '+':
            return False
    return True

num_cases = input_file.readline()

i = 1
n = 0
result = ''
for line in input_file:
    pancakes, k = line.split(" ")
    k = int(k)
    pancakes = list(pancakes)
    n = 0
    for x in range(len(pancakes) - int(k) + 1):
        pancake = pancakes[x]
        if pancake == '-':
            flip(pancakes, x, k)
            n += 1
    if happy(pancakes):
       result += "Case #{}: {}\n".format(i, n)
    else:
       result += "Case #{}: {}\n".format(i, "IMPOSSIBLE")
    i += 1

output_small = open('./result-large.txt', 'w+')
output_small.write(result)


