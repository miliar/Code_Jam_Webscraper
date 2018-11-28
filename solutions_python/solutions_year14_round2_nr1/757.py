def check_strings(strings):

    #first check if the strings aren't the same
    current_string = strings[0]
    if current_string == strings[1]:
        if len(strings) == 2:
            return True
        else:
            #iterate ovear all rest strings and compare them
            for i in range(1, len(strings)):
                if strings[i] != current_string:
                    return False
                current_string = strings[i]
        return True



def repeater_game(strings):

    #first check if is possible to finish game in 0 moves (all strings are 
    #identical)

    if check_strings:
        return '0'

    # now check if it is possible to win the game. After removing duplicates
    # all strings need to be the same
    no_duplicates = [''.join(set(sting)) for string in strings]
    if not check_strings:
        return 'Fegla Won'



def small(strings):

    if strings[0] == strings[1]:
        return 0

    first = strings[0]
    second = strings[1]

    #check if it is possible to win the 
    
    # now count how much does it take to win the game first == second
    root = set(first)


    #create dictionary where each key is the letter of the string and the value
    #is the number of occurences that letter in both first and second string

    first_dict, first = no_cons_string(first)
    second_dict, second = no_cons_string(second)
   


    
    #now iterate over all letters in both strings and calculate the absolute 
    #difference beteween number of letters in both strings
    #the solution is possible only if the length of both dicts is identical
    if len(first_dict) == len(second_dict) and first==second:
        result = 0 
        for i in range(1, len(first_dict)+1):
            result += abs(first_dict[i] - second_dict[i])
        return result
    return 'Fegla Won'





def no_cons_string(string):

    output = {1: 1}
    current_letter = string[0]
    current_position = 1
    letter_number = 1
    word = string[0]

    for i in range(1, len(string)):
        if string[i] == current_letter:
            letter_number += 1
            output[current_position] = letter_number
        else:
            current_letter = string[i]
            current_position += 1
            letter_number = 1
            output[current_position] = letter_number
            word += string[i]
            
    return output, word


if __name__ == '__main__':
    

    
    f = open('A-small-attempt4.in', 'rb')

    lines = f.readlines()
    cases = int(lines[0])
    results = []
    
    for i in range(2,len(lines),3):
        if lines[i+1][-1] != '\n':
            first = lines[i][:-1]
            second = lines[i+1]
        else:
            first = lines[i]
            second = lines[i+1]
        print first, second
        current = small([first, second])
        results.append(current)
        print current


    
    #write down the results to file
    output = open('outputSmall.in', 'wb')

    for i in range(cases):
        a = 'Case #' + str(i+1) + ': ' + str(results[i])
        
        output.write(a + '\n')

    output.close()
    # a = 'pdttfffhhhhhhhiiiiveqqvzzzzzzzzleylllxwwytiiiffpbbbnaeffaaavwwwwwggq'
    # b = 'ppdtfffffhhhhivveqvvvzzzleeeylxwwwyttifpbbbbbbnaeefaaaavwwgq'
    

    # print set(a) == set(b)

    # print small([a,b])
