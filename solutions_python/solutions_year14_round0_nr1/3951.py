def main():
    i = open('one.in')
    numCase = eval(i.readline())
    for x in range (numCase):
        row = eval(i.readline())

        lst1 = []
        for y in range (4):
            line = i.readline()
            if y == row-1:
                lst1 = line.split()
        col = eval(i.readline())
        lst2 = []
        for y in range (4):
            line = i.readline()
            if y == col-1:
                lst2 = line.split()
        lst3 = []
        for y in range (len(lst2)):
            if lst1[y] in lst2:
                lst3.append(lst1[y])
        if len(lst3) == 1:
            print ("Case #" + str(x+1) + ": " + lst3[0])
        elif len(lst3) >1:
            print ("Case #" + str(x+1) + ": Bad magician!")
        elif len(lst3) == 0:
            print ("Case #" + str(x+1) + ": Volunteer cheated!")

main ()
