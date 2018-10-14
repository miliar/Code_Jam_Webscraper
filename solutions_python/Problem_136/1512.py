import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
input = args.input
output = args.output
print "Reading input file", input

inputfile = open(input, "r")
outputfile = open(output, "w")

cases = int(inputfile.readline())
print "There are", cases, "test cases"

for i in range(0, cases):
    values = inputfile.readline().split()
    c = float(values[0])
    f = float(values[1])
    x = float(values[2])

    j = 1
    rate = 2.0
    answer = x / rate
    farm_time = 0
    while True:
        farm_time += c / rate
        rate += f
        new_answer = x / rate + farm_time
        if new_answer > answer:
            break
        else:
            answer = new_answer

    outputfile.write("Case #" + str(i + 1) + ": ")
    outputfile.write(str(answer))
    outputfile.write("\n")

inputfile.close()
outputfile.close()
