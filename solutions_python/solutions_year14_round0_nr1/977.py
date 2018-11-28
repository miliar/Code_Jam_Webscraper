input_fname = "input.txt"
output_fname = "output.txt"
lines = [line.strip() for line in open(input_fname)]

lines_per_test = 10

def solve(inputs):
    index_1 = int(inputs[0])
    set_1 = inputs[index_1].split(' ')
    index_2 = int(inputs[5])
    set_2 = inputs[5 + index_2].split(' ')
    intersection = set(set_1) & set(set_2)
    size = len(intersection)
    if size > 1:
        return 'Bad magician!'
    elif size == 0:
        return 'Volunteer cheated!'
    else:
        return intersection.pop()

def format_output(test_num, result):
    return "Case #" + str(test_num) + ": " + result + "\n"

fout = open(output_fname, "w")
for i in range(0,int(lines[0])):
    ans = solve(lines[i*lines_per_test+1:(i+1)*lines_per_test+1])
    fout.write(format_output(i+1,ans))
fout.close()
    
