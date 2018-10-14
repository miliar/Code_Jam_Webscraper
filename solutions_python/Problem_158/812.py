__author__ = 'chamathsilva'

def finder (data_String):
    data = [int(x) for x in data_String.split()]
    X = data[0]
    R = data[1]
    C = data[2]

    Area = R * C

    if X >= 7:
        return "RICHARD"
    elif X == 1:
        return "GABRIEL"
    elif X == 2:
        if (Area % 2 == 0) :
            return "GABRIEL"
        else:
            return "RICHARD"
    elif X == 3:
        if (R == 1) or (C == 1) or (Area % 3 != 0):
            return "RICHARD"
        else:
            return "GABRIEL"

    elif X == 4:
        if (Area % 4 != 0 ) or (R < 3) or (C <3 ) or ((R < 4) and (C < 4)):
            return "RICHARD"
        else:
            return "GABRIEL"

    elif X == 5:
        if (Area % 5 != 0) or (R < 3) or (C < 3) or ((R < 5) and (C < 5)):
             return "RICHARD"
        else:
            return "GABRIEL"
    elif X == 6:
        if (Area % 6 != 0) or (R < 3) or (C < 3) or ((R < 6) and (C < 6)):
            return "RICHARD"
        else:
            return "GABRIEL"


def get_input():
    out_string = ""
    input_file =  open('D-small-attempt1.in', 'r')
    N = int(input_file.readline())

    for i in range (N):
        temp = input_file.readline()
        out_string += str("Case #") + str(i+1) +str(": ")  + str(finder(temp)) + str("\n")
    output_file  = open('output_ominous.out','w')
    output_file.write(out_string)




if __name__ == "__main__":
    get_input()




















