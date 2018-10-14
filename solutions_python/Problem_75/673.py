#Magicka Google Code Jam Problem
#By Sean Egan

i = 0
total_combos = []   #combo letters/elements
combo_array = []
combo_double_array = []
total_opposers = [] #opposing letters/elements
opposer_array = []
opposer_double_array = []
element_length = [] #How many elements are being invoked
elements_array = []
elements_double_array = []
file_ = open('B-large.txt','r')
for line in file_:
    i = i + 1
    if (i==1):
        total_cases = int(line)
    else:
        split_line = line.split(' ')
        total_combos.append(int(split_line[0]))
        a = 1
        for x in range (1,int(split_line[0])+1):
            for letters in split_line[x]:
                combo_array.append(letters)
            a = a + 1
        total_opposers.append(int(split_line[a]))
        b = 1
        for x in range (a+1,a+1+int(split_line[a])):
            for letters in split_line[x]:
                opposer_array.append(letters)
            b = b + 1
        element_length.append(int(split_line[b+a]))
        for letters in split_line[b+a+1]:
            if ( letters != '\n'):
                elements_array.append(letters)

        combo_double_array.append(combo_array)
        combo_array = []
        opposer_double_array.append(opposer_array)
        opposer_array = []
        elements_double_array.append(elements_array)
        elements_array = []

for x in range(0,total_cases):
    first_array = []
    for i in range(0,element_length[x]):
        if (i == 0):
            first_array.append(elements_double_array[x][i])
        else:
            is_combo = False
            for a in range (0, total_combos[x]*3):
                if(a%3==0):
                    if(combo_double_array[x][a] == elements_double_array[x][i] and
                       combo_double_array[x][a+1] == first_array[i-1]):
                        is_combo = True
                        first_array[i-1] = '0'
                        first_array.append(combo_double_array[x][a+2])
                elif(a%3==1):
                    if(combo_double_array[x][a] == elements_double_array[x][i] and
                       combo_double_array[x][a-1] == first_array[i-1]):
                        is_combo = True
                        first_array[i-1] = '0'
                        first_array.append(combo_double_array[x][a+1])

            if(not is_combo):
                found_opposer = False
                for b in range(0, total_opposers[x]*2):
                    if(b%2 == 0):
                        if(opposer_double_array[x][b] == elements_double_array[x][i]):
                            for c in range(0,len(first_array)):
                                if (first_array[c] == opposer_double_array[x][b+1]):
                                    found_opposer = True
                    elif(b%2 == 1):
                        if(opposer_double_array[x][b] == elements_double_array[x][i]):
                            for c in range(0,len(first_array)):
                                if (first_array[c] == opposer_double_array[x][b-1]):
                                    found_opposer = True
          
                if(found_opposer):
                    for d in range(0,i):
                        first_array[d] = '0'
                    first_array.append('0')
                else:
                    first_array.append(elements_double_array[x][i])

    final_array = 'Case #{0}: [' .format(x+1)
    first_letter = True
    for letters in first_array:
        if (letters != '0'):
            if(first_letter): 
                final_array = final_array + letters
                first_letter = False
            else:
                final_array = final_array + ', ' 
                final_array = final_array + letters
    final_array = final_array + ']'
    print final_array

            




#print total_cases
#print total_combos
#print total_opposers
#print element_length
#print combo_double_array
#print opposer_double_array
#print elements_double_array




