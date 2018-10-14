def int_string_to_array(int_string):
    return list(map(int, int_string))

file = open('A-large.in', 'r')
lines = file.readlines()
num_test = lines[0][0]
lines = lines[1:]
result = []
for line in lines:
    line = line.split()
    max_shy = line[0]
    ppl_array = int_string_to_array(line[1])
    current_ppl = 0
    need_ppl = 0
    for i in range(int(max_shy)+1):
        if i > current_ppl:
            need_ppl += (i - current_ppl)
            current_ppl += (i - current_ppl)
        current_ppl += ppl_array[i]
    result.append(need_ppl)
file.close()

file = open("result.txt", 'w')
for i in range(len(result)):
    file.write("Case #" + str(i+1) + ": " + str(result[i]) + '\n')