f = open('workfile.txt', 'r')
i = 0
array = []
for line in f:
        array.append(map(int, line.split()))
limit = int(''.join(map(str,array[0])))
for i in range (0, limit):
    guess_1 = array[1 + i*10][0]
    numbersinguess_1 = array[1 + i*10 + guess_1]
    guess_2 = array[6 + i*10][0]
    numbersinguess_2 = array[6 + i*10 + guess_2]
    i = i + 1
    
    if len(set(numbersinguess_1).intersection(numbersinguess_2)) == 1:
        print ("Case #" + str(i) + ": " + str(set(numbersinguess_1).intersection(numbersinguess_2).pop()))
    if len(set(numbersinguess_1).intersection(numbersinguess_2)) < 1:
        print ("Case #" + str(i) + ": " + "Volunteer cheated!")
    if len(set(numbersinguess_1).intersection(numbersinguess_2)) > 1:
        print ("Case #" + str(i) + ": " +"Bad magician!")            
