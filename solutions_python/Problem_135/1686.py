#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andy
#
# Created:     11/04/2014
# Copyright:   (c) Andy 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def MakeList(text):
    text = text[:len(text) - 1]
    array = text.split()
    newarray = []
    for f in array:
        newarray.append(int(f))
    return newarray
def main():
    input_text = open("C:\Users\Andy\Downloads\A-small-attempt8.in")
    output_text = open("magictrick_output4.txt","w")
    Test_cases = input_text.readline()
    Test_cases = int(Test_cases)
    casenum = 0
    while casenum < Test_cases:
        casenum += 1
        x = input_text.readline()
        x = int(x)
        array1 = MakeList(input_text.readline())
        array2 = MakeList(input_text.readline())
        array3 = MakeList(input_text.readline())
        array4 = MakeList(input_text.readline())
        cards1 = [array1,array2,array3,array4]

        y = input_text.readline()
        y =  int(y)
        array5 = MakeList(input_text.readline())
        array6 = MakeList(input_text.readline())
        array7 = MakeList(input_text.readline())
        array8 = MakeList(input_text.readline())
        cards2 = [array5,array6,array7,array8]
        cardsfound = []


        for f in cards1[x-1]:
            if f in cards2[y-1]:
                cardsfound.append(f)
        if len(cardsfound) == 1:
            output_text.write("Case #" + str(casenum) + ": " + str(cardsfound[0]))
        elif len(cardsfound) >= 2:
            output_text.write("Case #" + str(casenum) + ": " + "Bad magician!")
        elif len(cardsfound) == 0 :
            output_text.write("Case #" + str(casenum) + ": " + "Volunteer cheated!")
        if not casenum == Test_cases:
            output_text.write("\n")
    output_text.close()




if __name__ == '__main__':
    main()
