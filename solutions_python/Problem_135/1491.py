#input read
input_file = open("input0.in", 'rt')
num_cases = int(input_file.readline())

#output write
output_file = open("output0.txt", 'w')

# do the job
def main_job(lines):
    first_answer = int(lines[0])
    first_line = [ int(x) for x in lines[first_answer].split() ]
    second_answer = int(lines[5])
    second_line = [ int(x) for x in lines[second_answer+5].split() ]
    found = 0
    for elem in first_line:
        if elem in second_line:
            if found != 0:
                return -1
            found = elem
    return found

for i in range(num_cases):
    lines = []
    for j in range(10):
        lines.append(input_file.readline())
    result = main_job(lines)
    if result > 0 :
        output = "Case #%d: %d\n" %(i+1, result)
    elif result == 0:
        output = "Case #%d: Volunteer cheated!\n" %(i+1)
    else:
        output = "Case #%d: Bad magician!\n" %(i+1)
    output_file.write(output)

input_file.close()
output_file.close()