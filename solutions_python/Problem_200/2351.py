# GCJ 2017 B-small

infile = open("B-large.in", "r")
outfile = open("B-large-result.txt", "w")

T = int(infile.readline())
for case in range(T):
    line = infile.readline()
    number = line[:-1]
    array = []
    for char in number:
        array.append(int(char))
    for i in range(2, len(number) + 1):
        if array[-i] > array[-(i-1)]:
            array[-i] = array[-i] - 1
            for j in range(1, i):
                array[-j] = 9
    answer = ""
    for digit in array:
        answer += str(digit)

    outfile.write("Case #{0}: {1}\n".format(str(case + 1), int(answer)))

infile.close()
outfile.close()
