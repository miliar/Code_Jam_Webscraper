def main():
    tab1 = 'abcdefghijklmnopqrstuvwxyz'
    tab2 = 'yhesocvxduiglbkrztnwjpfmaq'
    f1 = open('A-small-attempt2.in', 'r')
    f2 = open('output.out', 'w')
    t = int(f1.readline().strip("\n"))
    for j in range(t):
        theInput = f1.readline().strip("\n")
        theOutput = "Case #" + str(j+1) + ": "
        for index in range(0, len(theInput), 1):
            if theInput[index] == ' ':
                    theOutput = theOutput + ' ';
            else:
                    for i in range(0, len(tab1), 1):
                            if theInput[index] == tab1[i]:
                                    theOutput = theOutput + tab2[i]
        f2.write(theOutput + "\n")
    f1.close()
    f2.close()

main()
