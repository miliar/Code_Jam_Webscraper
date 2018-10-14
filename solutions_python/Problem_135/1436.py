data = input ()
data = data.split('\n')
cases = int(data[0])
data = data [1:]

for c in range (0, cases):
    first_num = int(data [c*10])
    first_row = data [c*10 + first_num]
    second_num = int(data [c*10 + 5])
    second_row = data [c*10 +5+ second_num]
    first_row = first_row.split()
    second_row = second_row.split()
    sol = 0
    num = 0
    for card in first_row:
        if card in second_row:
            sol +=1
            num = card
    print ('Case #' + str(c+1) + ': ', end=''),
    if sol ==0:
        print ('Volunteer cheated!')
    elif sol == 1:
        print (num)
    else:
        print ('Bad magician!')
        
