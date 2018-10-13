def get_card_list(f):
    card_list = []
    for i in range(4):
        s = f.readline().strip()
        card_row = s.split(" ")
        card_list.append(card_row)
    return card_list


f = open("A-small-attempt0.in")
f1 = open("output.txt","w")

s = f.readline()
test_case = int(s.strip())

card_list1 = []
card_list2 = []
for i in range(test_case):
    s = f.readline()
    row_1 = int(s.strip())
    card_list1 = get_card_list(f)
    s = f.readline()
    row_2 = int(s.strip())
    card_list2 = get_card_list(f)

    flag = 0
    value = ""

    for j in card_list1[row_1-1]:
        if j in card_list2[row_2-1]:
            flag += 1
            value = j

    if(flag == 1):
        f1.write("Case #"+str(i+1)+": "+value+"\n")
    elif(flag == 0):
        f1.write("Case #"+str(i+1)+": "+"Volunteer cheated!"+"\n")
    else:
        f1.write("Case #"+str(i+1)+": "+"Bad magician!"+"\n")

f.close()
f1.close()
