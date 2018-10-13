def get_list_of_card(w):
    list_card = []
    for a in range(4):
        q = w.readline().strip()
        row_of_card = q.split(" ")
        list_card.append(row_of_card)
    return list_card


file1 = open("A-small-attempt1.in")
file2 = open("output.txt","w")

q = file1.readline()
num_case = int(q.strip())

list_card1 = []
list_card2 = []

for i in range(num_case):
    q = file1.readline()
    row_1 = int(q.strip())
    list_card1 = get_list_of_card(file1)
    q = file1.readline()
    row_2 = int(q.strip())
    list_card2 = get_list_of_card(file1)

    flag1 = 0
    result = ""

    for j in list_card1[row_1-1]:
        if j in list_card2[row_2-1]:
            flag1 += 1
            result = j

    if(flag1 == 1):
        file2.write("Case #"+str(i+1)+": "+result+"\n")
    elif(flag1 == 0):
        file2.write("Case #"+str(i+1)+": "+"Volunteer cheated!"+"\n")
    else:
        file2.write("Case #"+str(i+1)+": "+"Bad magician!"+"\n")

		
file1.close()
file2.close()
