
n = int(raw_input())
c = 1;
while (n):
    n = n - 1;
    l1 = raw_input()
    l2 = raw_input()
    l3 = raw_input()
    l4 = raw_input()
    a = raw_input()
    output = ""

    if l1.replace("X", "T") == "TTTT" or l2.replace("X", "T") == "TTTT" or l3.replace("X", "T") == "TTTT" or l4.replace("X", "T") == "TTTT":
        output = "X won"
    elif l1.replace("O", "T") == "TTTT" or l2.replace("O", "T") == "TTTT" or l3.replace("O", "T") == "TTTT" or l4.replace("O", "T") == "TTTT":
        output = "O won"
    elif l1.replace("X", "T")[0] + l2.replace("X", "T")[0] + l3.replace("X", "T")[0] + l4.replace("X", "T")[0] == "TTTT":
        output = "X won"
    elif l1.replace("X", "T")[1] + l2.replace("X", "T")[1] + l3.replace("X", "T")[1] + l4.replace("X", "T")[1] == "TTTT":
        output = "X won"
    elif l1.replace("X", "T")[2] + l2.replace("X", "T")[2] + l3.replace("X", "T")[2] + l4.replace("X", "T")[2] == "TTTT":
        output = "X won"
    elif l1.replace("X", "T")[3] + l2.replace("X", "T")[3] + l3.replace("X", "T")[3] + l4.replace("X", "T")[3] == "TTTT":
        output = "X won"
    elif l1.replace("X", "T")[0] + l2.replace("X", "T")[1] + l3.replace("X", "T")[2] + l4.replace("X", "T")[3] == "TTTT":
        output = "X won"
    elif l1.replace("X", "T")[3] + l2.replace("X", "T")[2] + l3.replace("X", "T")[1] + l4.replace("X", "T")[0] == "TTTT":
        output = "X won"

    elif l1.replace("O", "T")[0] + l2.replace("O", "T")[0] + l3.replace("O", "T")[0] + l4.replace("O", "T")[0] == "TTTT":
        output = "O won"
    elif l1.replace("O", "T")[1] + l2.replace("O", "T")[1] + l3.replace("O", "T")[1] + l4.replace("O", "T")[1] == "TTTT":
        output = "O won"
    elif l1.replace("O", "T")[2] + l2.replace("O", "T")[2] + l3.replace("O", "T")[2] + l4.replace("O", "T")[2] == "TTTT":
        output = "O won"
    elif l1.replace("O", "T")[3] + l2.replace("O", "T")[3] + l3.replace("O", "T")[3] + l4.replace("O", "T")[3] == "TTTT":
        output = "O won"
    elif l1.replace("O", "T")[0] + l2.replace("O", "T")[1] + l3.replace("O", "T")[2] + l4.replace("O", "T")[3] == "TTTT":
        output = "O won"
    elif l1.replace("O", "T")[3] + l2.replace("O", "T")[2] + l3.replace("O", "T")[1] + l4.replace("O", "T")[0] == "TTTT":
        output = "O won"
    elif "." in l1+l2+l3+l4:
        output = "Game has not completed"
    else:
        output = "Draw"

    

    print "Case #"+`c`+": "+output
    c = 1 + c;