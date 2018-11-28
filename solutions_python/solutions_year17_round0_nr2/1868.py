def process(num):
    l = list(str(num))
    index = -1
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            index = i
            for j in range(index-2, -1, -1):
                if l[j] == l[index-1]:
                    index = j+1
                else:
                    break
            break
    if index == -1:
        return num  # number is tidy

    tosub = int(''.join(l[index:])) + 1
    tmp = num - tosub
    return tmp


inp = open("input/B-large.in", "r")
out = open("output/large.out", "w")
lines = inp.read().split("\n")

line_count = int(lines[0])

for i in range(1, line_count + 1):
    number = int(lines[i])
    out.write("Case #" + str(i) + ": " + str(process(number)) + "\n")
