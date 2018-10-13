__author__ = 'parad0x'

my_file = open("A-small-attempt0.in","r")
cases = int(my_file.readline())

for t in range(cases):
    a1  = int(my_file.readline().rstrip('\n'))
    r1a = my_file.readline().rstrip('\n')
    r2a = my_file.readline().rstrip('\n')
    r3a = my_file.readline().rstrip('\n')
    r4a = my_file.readline().rstrip('\n')

    a2  = int(my_file.readline().rstrip('\n'))
    r1b = my_file.readline().rstrip('\n')
    r2b = my_file.readline().rstrip('\n')
    r3b = my_file.readline().rstrip('\n')
    r4b = my_file.readline().rstrip('\n')

    fElements = []
    sElements = []

    if a1 == 1:
        fElements = r1a.split(' ')
    elif a1 == 2:
        fElements = r2a.split(' ')
    elif a1 == 3:
        fElements = r3a.split(' ')
    elif a1 == 4:
        fElements = r4a.split(' ')

    if a2 == 1:
        sElements = r1b.split(' ')
    elif a2 == 2:
        sElements = r2b.split(' ')
    elif a2 == 3:
        sElements = r3b.split(' ')
    elif a2 == 4:
        sElements = r4b.split(' ')

    counter = 0
    card_number = 0
    for y in range(4):
        for z in range(4):
            if fElements[y] == sElements[z]:
                card_number = fElements[y]
                counter += 1

    if counter == 1:
        print("Case #" + str(t+1) + ":",card_number)
    elif counter > 1:
        print ("Case #" + str(t+1) + ": Bad magician!")
    elif counter == 0:
        print ("Case #" + str(t+1) + ": Volunteer cheated!")

my_file.close()
