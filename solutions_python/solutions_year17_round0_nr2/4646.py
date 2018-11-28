def is_tidy(number):
    number = str(number)
    res = True
    for x in range(len(number) - 1):
        if int(number[x]) > int(number[x + 1]):
            res = False
            break
    return res

results = []
lines = []
with open('test.in') as f:
    for line in f:
        lines.append(line.strip())

lines.pop(0)
for index, line in enumerate(lines):
    while not is_tidy(line):
        line = str(int(line) - 1)
    results.append("Case #" + str(index +1 ) + ": " + line)

with open('res.txt', 'w') as f:
    for x in results:
        f.write(x + "\n")




