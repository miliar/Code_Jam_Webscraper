input = open('A-large.in', 'r')
output = open('A-large.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    data = input.readline().rstrip().split()
    smax = int(data[0])
    s = data[1]
    ans = 0
    sum = 0
    for i in range(smax + 1):
        if i > sum:
            ans += i - sum
            sum = i
        sum += int(s[i])
    output.write("Case #" + str(test + 1) + ": " + str(ans) + "\n")

input.close()
output.close()