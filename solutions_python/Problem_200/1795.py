
f_in = open('B-large.in', 'r')

data = f_in.readlines()

f_in.close()

for i in range(len(data)):
    data[i] = data[i][0:len(data[i])-1]

l = []
sol = []

cases = int(data.pop(0))

for i in range(cases):
    num = list(data[i])
    for j in range(len(num)):
        num[j] = int(num[j])
    l.append(num)


print('Calculating')

for i in range(cases):
    n = l[i]
    for entry in n:
        entry = int(entry)
    at = 0
    while at < len(n) - 1:
        if n[at + 1] >= n[at]:
            at += 1
        else:
            n[at] -= 1
            for j in range(at + 1, len(n)):
                n[j] = 9
            if at != 0:
                at -= 1
    while True:
        if n[0] == 0:
            n.pop(0)
        else:
            break
    for j in range(len(n)):
        n[j] = str(n[j])
    sol.append('Case #' + str(i+1) + ': ' + ''.join(n))

f = open('tidy_numbers_large.txt', 'w')
for entry in sol:
    f.write(entry + '\n')
f.close()

print('Done')
