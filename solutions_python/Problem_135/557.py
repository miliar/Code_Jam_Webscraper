__author__ = 'Pierre-Luc'


def solve(answer,cards,numCase):

    rowChosen = []
    rowChosen.append(cards[0][answer[0]-1])
    rowChosen.append(cards[1][answer[1]-1])

    solutions = []

    for i in rowChosen[0]:
        for j in rowChosen[1]:
            if i==j:
                solutions.append(str(i))

    print("Case#:" +str(numCase+1))
    print(" ".join(solutions))

    fOutput.write("Case #" + str(numCase+1) + ": ")
    if len(solutions)==0:
        fOutput.write("Volunteer cheated!")
    elif len(solutions)>1:
        fOutput.write("Bad magician!")
    else:
        fOutput.write(str(solutions[0]))
    fOutput.write("\n")




print("owoo")
list = [1]
a = 1

fInput = open("1InputSmall.txt","r")
fOutput = open("1OutputSmall.txt","w")


T = int(fInput.readline())

for numCase in range(0,T):
    cards = []
    answer = []
    for j in range(0,2):

        answer.append(int(fInput.readline()))
        cards.append([])
        for k in range(0,4):
            line = fInput.readline().strip("\n").split(" ")
            line = [int(i) for i in line]
            cards[j].append(line)

    solve(answer,cards,numCase)

