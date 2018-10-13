T = int(input())
combos = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:9}
correct = {"0": 0, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "10":0}
def tidy(value):
    number = int(value)
    curNo = list(combos)[-1]
    listN = map(str,list(str(value)))
    nth = 1
    while check(number) == False:
        if listN[-nth] == "9":
            nth = nth + 1
        else:
            listN[-nth] = "9"
            listN[-nth - 1] = str(int(listN[-nth-1])-1)
            #print(str(listN) + "HERE" + str(nth))
            while listN[-nth -1] == "-1":
                listN[-nth - 1] = "9"
                #print(str(listN) + "HERE2" + str(nth))
                nth = nth + 1
                listN[-nth - 1] = str(int(listN[-nth-1])-1)
            number = int("".join(listN))
    combos[value] = number
    return combos[value]
    
def check(checkN):
    listN = map(str,list(str(checkN)))
    if str(checkN) in correct:
        if correct[str(checkN)] == 1:
            return True
        else:
            return False
    else:
        if int(listN[0]) > int(listN[1]):
            correct[str(checkN)] = 0
            return False
        else:
            if check(int("".join(listN[1:]))):
                correct[str(checkN)] = 1
                return True
            else:
                correct[str(checkN)] = 0
                return False

for x in range(T):
    limit = input()
    print("Case #" + str(x+1) +": "+ str(tidy(limit)))
    #print(combos)
    #print(correct)
    
