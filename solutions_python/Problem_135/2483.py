def foo(choice1, grid1, choice2, grid2):
    answer = 0
    count = 0
    for i in grid1[choice1-1]:
        if i in grid2[choice2-1]:
            answer = i
            count += 1
    if answer == 0:
        return "Volunteer cheated!"
    if count == 1:
        return answer
    return "Bad magician!"


file = open("A-small-attempt0.in.txt", "r")
output = open("outputSmallA.txt", "w")
for i in range(int(file.readline())):
    choice1 = int(file.readline())
    grid1 = []
    for j in range(4):
        grid1.append([int(n) for n in file.readline().split()])
        
    choice2 = int(file.readline())
    grid2 = []
    for j in range(4):
        grid2.append([int(n) for n in file.readline().split()])

    output.write("Case #" + str(i+1) + ": " + str(foo(choice1, grid1, choice2, grid2)) + "\n")

file.close()
output.close()
