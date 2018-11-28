from math import * 

###################################################################
##################### Misc Functions ##############################
###################################################################

############### transpose ##########################################

def transpose(string):
    """ seperates lines and words into nested lists """
    
    data = []
    linedata = []
    worddata = []
    for letter in string:
        if letter == "\n":
            linedata.append(worddata)
            data.append(linedata)
            linedata = []
            worddata = []
        elif letter == " ":
            linedata.append(worddata)
            worddata = []
        else:
            worddata.append(letter)
    linedata.append(worddata)
    data.append(linedata)
    return data


############### get_num ###########################################

def get_num(digits):
    """ retreaves the number that is made up of these digits and symbols """

    number = 0
    sign = 1
    digit_number = 0
    decimal = 0
    number_of_digits = len(digits)
    
    for digit in digits:
        if digit == "-":
            sign = -1
            digit_number += 1
        elif digit == ".":
            decimal = number_of_digits - digit_number
        else:
            number += int(digit)*(10**(number_of_digits-digit_number-1))
            digit_number += 1
            
    return float(number*sign)/(10**decimal)

############### get_word ##########################################

def get_word(letters):
    """ concatenates letters into a word """

    word = ""
    for letter in letters:
        word += letter 
       
    return word


###################################################################
##################### Saving the Universe #########################
###################################################################

def arrange_message(nested_lists):
    num_cases = get_num(nested_lists[0][0])
    line = 1
    arranged_list = []
    for case in range(int(num_cases)):
        new_case = []
        engine_number = int(get_num(nested_lists[line][0]))
        line += 1
        new_engine = []
        for engine in nested_lists[line:line+engine_number]:
            engine_name = ""
            for word in engine:
                engine_name += get_word(word) + " "
            engine_name = engine_name[:-1]
            new_engine.append(engine_name)
        new_case.append(new_engine)
        
        line += engine_number
        query_number = int(get_num(nested_lists[line][0]))
        line += 1
        new_query = []
        for query in nested_lists[line:int(line+query_number)]:
            query_name = ""
            for word in query:
                query_name += get_word(word) + " "
            query_name = query_name[:-1]
            new_query.append(query_name)
        new_case.append(new_query)
        line += query_number

        arranged_list.append(new_case)
                                
    return arranged_list

def saving_the_universe(arranged_message):
    case_num = 1
    for case in arranged_message:

        engine_names = case[0][:]
        queries = case[1]

        change_count = 0
        query_index = 0
        query_number = len(queries)
        while query_index < query_number:
            query_name = queries[query_index]
            if queries[query_index] in engine_names:
                engine_names.remove(query_name)
            if engine_names == []:
                change_count += 1
                engine_names = case[0][:]
                engine_names.remove(query_name)
            query_index += 1

        print "Case #%s: " % case_num, change_count

        case_num += 1
            


