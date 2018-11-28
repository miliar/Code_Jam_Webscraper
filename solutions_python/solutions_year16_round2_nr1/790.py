def getting_digits(file_name):
    read_file_name = file_name
    write_file_name = file_name + ' - answer.txt'
    
    read_file = open(read_file_name)
    write_file = open(write_file_name, "w")
    
    cases = int(read_file.readline())
    
    current_case = 1
    
    while current_case <= cases:
        word = read_file.readline().rstrip()
        output = "Case #{0}: {1}\n".format(current_case, word_to_digits(word))
        print(word)
        print(output)
        write_file.write(output)
        current_case += 1
        

def word_to_digits(word):
    char_frequency = {}
    for char in  word:
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] = char_frequency[char] + 1
    
    word_frequency = {}
    
    word_frequency[0] = number_of_occurrences(char_frequency, "Z", "ERO")
    word_frequency[2] = number_of_occurrences(char_frequency, "W", "TO")
    word_frequency[6] = number_of_occurrences(char_frequency, "X", "SI")
    word_frequency[8] = number_of_occurrences(char_frequency, "G", "EIHT")
    word_frequency[3] = number_of_occurrences(char_frequency, "H", "TREE")
    word_frequency[4] = number_of_occurrences(char_frequency, "R", "FOU")
    word_frequency[5] = number_of_occurrences(char_frequency, "F", "IVE")
    word_frequency[1] = number_of_occurrences(char_frequency, "O", "NE")
    word_frequency[7] = number_of_occurrences(char_frequency, "V", "SEEN")
    word_frequency[9] = number_of_occurrences(char_frequency, "I", "NNE")
    
    output = ""
    
    for i in range(0, 10):
        output += str(i) * word_frequency[i]
    
    return output
    

def number_of_occurrences(char_frequency, key_letter, other_letters):
    if key_letter not in char_frequency:
        return 0
    else:
        occurrences = char_frequency[key_letter]
        if occurrences == 0:
            return 0
        char_frequency[key_letter] = 0
        for char in other_letters:
            char_frequency[char] -= occurrences
        return occurrences
        


if __name__ == "__main__":
    getting_digits("test.txt")
    #getting_digits("A-small-attempt1.in")
    getting_digits("A-large.in")