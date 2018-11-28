with open('A-small-attempt1.in', 'r') as a:
    text = a.readlines()
    a.close()
b = open('A-small-attempt1.out', 'w+')
cases = int(text[0])
for i in range(0, cases):
    firstAnswer = int(text[10 * i + 1])
    secondAnswer = int(text[10 * i + 6])
    firstAnswers = []
    num = ""
    for n in text[10 * i + firstAnswer + 1]:
        if (n == " ") or (n == "\n"):
            firstAnswers.append(int(num))
            num = ""
        else:
            num += n
    secondAnswers = []
    num = ""
    for n in text[10 * i + secondAnswer + 6]:
        if (n == " ") or (n == "\n"):
            secondAnswers.append(int(num))
            num = ""
        else:
            num += n
    cards = 0
    for n in firstAnswers:
        if n in secondAnswers:
            cards += 1
            result = n
    
    if cards == 1:
        b.write("Case #{}: {}\n".format(i + 1, result))
    elif cards > 1:
        b.write("Case #{}: {}\n".format(i + 1, "Bad magician!"))
    else:
        b.write("Case #{}: {}\n".format(i + 1, "Volunteer cheated!"))
b.close()