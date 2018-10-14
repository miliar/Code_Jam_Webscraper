def reduce(input, i):
    input[i] = input[i] - 1
    for j in range(i + 1, len(input)):
        input[j] = 9




def solve(input):
    input = list(map(int, input))
    print(input)
    while sorted(input) != input:
        for i in range(0, len(input) - 1):
            if input[i] > input[i + 1]:
                reduce(input, i)

    input = list(map(str, input))

    input = ''.join(input)
    return int(input)

with open('q1.txt') as text:
    content = text.readlines()

content = [x.strip() for x in content]

print(content)

casesCount = content[0]
print(casesCount)
with open('out.txt', 'w+') as out:
    for num in range(0, int(casesCount)):
        ans = solve(content[num + 1])
        print(ans)
        out.write('Case #{}: {}\n'.format(num + 1, ans))

# out.write('Case #{}: {}\n'.format(num + 1, solve(content[num + 1])))





