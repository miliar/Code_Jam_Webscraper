import sys
def to_ints(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def test(answer1, board1, answer2, board2):
    first = []
    possible = []
    for i in range(4):
        first.append(board1[(answer1 - 1) * 4 + i])
    for i in range(4):
        num = board2[(answer2 - 1) * 4  + i]
        if num in first:
            possible.append(num)
    if (len(possible)==0):
        return "Volunteer cheated!"
    if (len(possible)==1):
        return str(possible[0])
    return "Bad magician!"

input_file = open(sys.argv[1])
input = []
output = open("output.txt", "w")
for line in input_file:
    input.append(line)

for i in range(int(input[0])):
    index = i * 10
    answer1 = input[index + 1]
    board1 = ""
    for j in range(4):
        board1 += input[index + j + 2]
    answer2 = input[index + 6]
    board2 = ""
    for j in range(4):
        board2 += input[index + j + 7]
    board1 = board1.replace("\n", " ").split()
    board2 = board2.replace("\n", " ").split()
    output.write("Case #" + str(i + 1) + ": " + test(int(answer1), to_ints(board1), int(answer2), to_ints(board2)) + "\n")
    
