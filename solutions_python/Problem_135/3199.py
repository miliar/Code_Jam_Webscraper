def findcard():
    f = open("/Users/zulsarbatmunkh/Downloads/A-small-attempt2.in.txt")
    Input = f.read()
    print f
    rows = Input.split("\n")
    testcases = int(rows[0])
    answer = ""
    i=0
    while i<testcases:
        guess1 = int(rows[i*10+1])
        guess1row = rows[i*10+1+guess1].split(" ")
        guess2 = int(rows[i*10+6])
        guess2row = rows[i*10+6+guess2].split(" ")
        occurence = 0
        numz = ""
        for guess in guess1row:
            for num in guess2row:
                if int(guess)==int(num):
                    numz = guess
                    occurence+=1
        if occurence == 1:
            answer += "Case #" + str(i+1) + ": " + numz+"\n"
        elif occurence ==0 :
            answer += "Case #" + str(i+1) + ": " + "Volunteer cheated!\n"
        else:
            answer += "Case #" + str(i+1) + ": " + "Bad magician!\n"
        i+=1
    return answer[:-1]
input= "100\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n3\n1 2 5 4\n3 11 6 15\n9 10 7 12\n13 14 8 16"
input+= "\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16"
input+= "\n2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n3\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16"
 
print findcard()
