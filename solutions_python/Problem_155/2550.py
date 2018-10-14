input_file = open("A-large.in")
output_file = open("Standing Ovation.txt", 'w')
inp_list = input_file.readlines()
line_counter = 0
tc = int(inp_list[line_counter])
case_number = 0
for x in xrange(tc):
    case_number += 1
    line_counter += 1
    data = str(inp_list[line_counter]).split()
    seated = 0
    required = 0
    max_shy = int(data[0])
    people = data[1]
    shy_counter = 0
    while shy_counter <= max_shy:
        seated += int(people[shy_counter])
        if seated > shy_counter:
            shy_counter += 1
        else:
            required += 1
            seated += 1
            shy_counter += 1
    output_file.write('Case #' + str(case_number) + ': ' + str(required) + '\n')
output_file.close()
input_file.close()