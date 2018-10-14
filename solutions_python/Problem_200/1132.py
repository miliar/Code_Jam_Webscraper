import math

infile = open("B-large.in", "r")
outfile = open("Bout.txt", "w")

tcase = int(infile.readline().rstrip())
for z in range(1, tcase+1):
    number = infile.readline().rstrip()
    number = list(number)
    number = [int(i) for i in number]
    i = len(number) - 1
    while i > 0:
        if number[i] < 0:
            number[i] = .9
            number[i-1] -= 1
        if number[i] < number[i-1]:
            number[i] = 9
            number[i-1] -= 1
        i -= 1
    for i in range(0, len(number) - 1):
        if number[i+1] < number[i]:
            number[i+1] = number[i]
    final = 0
    for i in range(0, len(number)):
        final += number[i] * int(math.pow(10, len(number) - 1 - i))
    #print(final)
    outfile.write("Case #" + str(z) + ": " + str(final) + "\n");

outfile.close()
infile.close()
