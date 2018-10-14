def people_array(string):
    return list(map(int, string))

def answer(string):
    people = people_array(string)

    people_standing = 0
    to_invite = 0

    for shyness, persons in enumerate(people):
        if persons == 0:
            continue
        elif people_standing >= shyness:
            people_standing += persons
        else:
            to_invite += (shyness - people_standing)
            people_standing += (to_invite + persons)

    return to_invite

def interpret(lines):
    lines = lines.split("\n")[1:]

    result = ""

    for index, line in enumerate(lines):
        result += "Case #" + str(index + 1) + ": " + str(answer(line.split(" ")[1])) + "\n"

    return result[:-1]

file_in = open("input2.txt")
file_out = open("output.txt", "w+")
string = file_in.read()

result = interpret(string)

file_out.write(result)

file_in.close()
file_out.close()

#print(answer("0001001"))