
#f = open("./input.txt")
f = open("./a.in")

ans = open("A-small-ans", "w")

num = 0
flag = False
square1 = []
square2 = []
choose1 = 0
choose2 = 0
currentNum = 0
for line in f:
    num = num + 1

    if num == 1:
        probNum = int(line)
        #print "num prob:", probNum
        continue
    elif (num - 2) % 10 == 0:
        choose1 = int(line)
    elif (num - 2) % 5 == 0:
        choose2 = int(line)

    elif (num - 2) % 10 < 5:
        square1.append(map(int, line.split()))
    elif (num - 2) % 10 > 5:
        square2.append(map(int, line.split()))

    if (num - 1) % 10 == 0 and num -2 != 0:
        currentNum += 1
        """
        print choose1
        print square1
        print choose2
        print square2
        """

        ans = set(square1[choose1 - 1]) & set(square2[choose2 - 1])
        string = "Case #" + str(currentNum) + ": "
        if len(ans) == 0:
            print string + "Volunteer cheated!"
        elif len(ans) == 1:
            print string + str(list(ans)[0])
        else:
            print string + "Bad magician!"



        square1 = []
        square2 = []


"""
string = "Case #" + str(num - 1) + ":"
if flag == False:
string = string + " OFF\n"
else:
string = string + " ON\n"
print string
ans.write(string)
ans.close()
f.close()
"""
