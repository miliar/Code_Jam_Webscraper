import sys
import random


def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("\n", "")
    return line

def getSpace(initial):
    StartPos = []
    Size = []
    TempInt = 0
    j = 0
    while j <= len(Initial)-1:
        k = Initial[j]
        if k == "." and TempInt == 0:
            TempInt += 1
            StartPos.append(j+1)
        elif k == ".":
            TempInt += 1
        elif k == "O" and TempInt > 0:
            Size.append(TempInt)
            TempInt = 0
        j += 1


    Stop = "N"
    z = max(Size)
    j = 0
    while j <= len(Size)-1 and Stop == "N":
        k = Size[j]
        if k == z:
            Start = StartPos[j]
            Stop = "Y"
        else:
            j += 1

    Array = [z, Start]

    return Array


def getMiddle(z, Size, StartPos):
    if Size%2 == 0:
        Position = (StartPos-1) + (Size / 2)
    else:
        Position = (StartPos-1) + ((Size + 1) / 2)

    return Position


file = open("C-small-1-attempt0.in")
Count = int(next_line(file))
MaxA = []
MinA = []

i = 0
while i <= Count-1:
    z = next_line(file).split()
    N = int(z[0])
    K = int(z[1])

    Initial = "O" + ("." * N) + "O"

    ToiletA = []
    ToiletA.append(Initial)

    j = 0
    while j <= (K - 1):
        Initial = ToiletA[len(ToiletA)-1]
        z = getSpace(Initial)
        Size = z[0]
        StartPos = z[1]

        Position = int(getMiddle(z, Size, StartPos))

        Part1 = Initial[:(Position - 1)]
        Part2 = "O"
        Part3 = Initial[Position:]

        Final = Part1 + Part2 + Part3

        ToiletA.append(Final)
        j += 1

    Final = ToiletA[len(ToiletA)-1]


    Stop = "N"
    Left = 0
    LeftS = Final[:(Position-1)]
    j = len(LeftS)-1
    while j >= 0 and Stop == "N":
        k = LeftS[j]
        if k == ".":
            Left += 1
        else:
            Stop = "Y"
        j -= 1


    Stop = "N"
    Right = 0
    RightS = Final[Position:]
    j = 0
    while j <= len(RightS)-1 and Stop == "N":
        k = RightS[j]
        if k == ".":
            Right += 1
        else:
            Stop = "Y"
        j += 1

    MinA.append(min(Left, Right))
    MaxA.append(max(Left, Right))

    i += 1
file.close()


file = open_file("C output small.in", "a")
i = 0
while i <= Count-1:
    file.write("Case #" + str(i+1) + ": " + str(MaxA[i]) + " " + str(MinA[i]) + "\n")
    i += 1
file.close()
