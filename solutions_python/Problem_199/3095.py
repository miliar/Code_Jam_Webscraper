lines = []
with open("A-large.in", 'r') as reader:
   lines = reader.readlines()
t = int(lines[0])
lines = lines[1:]
out = open("1.out", 'w')

def solution(cakes, k):
    total = 0
    table = [True if c == '+' else False for c in cakes]
    i = 0
    while i < len(table) - k + 1:
        if not table[i]:
            for index in range(k):
                table[i + index] = not table[i + index]
            total += 1
        i += 1
    if not all(table[len(table) - k:]):
        return "IMPOSSIBLE"
    return total

for i in range(len(lines)):
    tokens = lines[i].split()
    out.write("Case #" + str(i + 1) + ': ' + str(solution(tokens[0], int(tokens[1]))) + "\n")

