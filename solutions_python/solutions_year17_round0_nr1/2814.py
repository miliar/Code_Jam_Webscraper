
def flip(k, index, pancakes):
    for i in range(index, index + k):
        pancakes[i] = 1 - pancakes[i]


def solve(input):
    flips = 0
    line = input.split(' ')
    pancakes = line[0]
    k = line[1]
    pancakes = pancakes.replace('+', '1')
    pancakes = pancakes.replace('-', '0')
    pancakes = list(pancakes)
    for i in range(0, len(pancakes)):
        pancakes[i] = int(pancakes[i])

    for i in range(0, len(pancakes) - int(k) + 1):
        if pancakes[i] == 0:
            flip(int(k), i, pancakes)
            flips +=1
    if 0 in pancakes:
        return 'IMPOSSIBLE'
    return str(flips)




with open('q1.txt') as text:
    content = text.readlines()

content = [x.strip() for x in content]

print(content)

casesCount = content[0]
print(casesCount)
with open('out.txt', 'w+') as out:
    for num in range(0, int(casesCount)):
        out.write('Case #{}: {}\n'.format(num + 1, solve(content[num + 1])))




