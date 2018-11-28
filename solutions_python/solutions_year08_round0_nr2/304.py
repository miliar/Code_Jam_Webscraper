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

def arrange_saving_message(nested_lists):
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


###################################################################
##################### Train Timetable #############################
###################################################################      

def train_transpose(string):
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
        elif letter == " " or letter == ":":
            linedata.append(worddata)
            worddata = []
        else:
            worddata.append(letter)
    linedata.append(worddata)
    data.append(linedata)
    return data

def arrange_train_message(nested_lists):
    num_cases = get_num(nested_lists[0][0])
    line = 1
    arranged_list = []
    for case in range(int(num_cases)):
        new_case = []
        wait_time = int(get_num(nested_lists[line][0]))
        line += 1
        AB_number = int(get_num(nested_lists[line][0]))
        BA_number = int(get_num(nested_lists[line][1]))
        line += 1
        AB_trains = []
        for train in nested_lists[line:line+AB_number]:
            new_train = [get_num(train[0])*60+get_num(train[1]), get_num(train[2])*60+get_num(train[3])]
            AB_trains.append(new_train)
        new_case.append(AB_trains)
        line += AB_number
        
        BA_trains = []
        for train in nested_lists[line:line+BA_number]:
            new_train = [get_num(train[0])*60+get_num(train[1]), get_num(train[2])*60+get_num(train[3])]
            BA_trains.append(new_train)
        new_case.append(BA_trains)
        line += BA_number
        
        new_case.append(wait_time)
        
        arranged_list.append(new_case)
                                
    return arranged_list

def train_timetable(arranged_message):
    case_num = 1
    for case in arranged_message:
        AB_trains = case[0]
        BA_trains = case[1]
        wait_time = case[2]

        AB_departures = [train[0] for train in AB_trains]
        AB_arrivals = [train[1] for train in AB_trains]
        BA_departures = [train[0] for train in BA_trains]
        BA_arrivals = [train[1] for train in BA_trains]

        extra_AB_trains = 0
        extra_BA_trains = 0

        AB_trains_used = 0
        BA_trains_used = 0
        
        for minute in range(60*24):
##            if minute > 300 and minute < 330:
##                print minute-1
##                print "waiting", extra_AB_trains, extra_BA_trains
##                print "totals used", AB_trains_used, BA_trains_used
            if (minute-wait_time) in BA_arrivals:
                BA_arrival_num = BA_arrivals.count(minute-wait_time)
                extra_AB_trains += BA_arrival_num
            if (minute-wait_time) in AB_arrivals:
                AB_arrival_num = AB_arrivals.count(minute-wait_time)
                extra_BA_trains += AB_arrival_num
            if minute in AB_departures:
                AB_departure_num = AB_departures.count(minute)
                if extra_AB_trains <= AB_departure_num:
                    AB_trains_used += (AB_departure_num - extra_AB_trains)
                    extra_AB_trains = 0
                else:
                    extra_AB_trains -= AB_departure_num
            if minute in BA_departures:
                BA_departure_num = BA_departures.count(minute)
                if extra_BA_trains <= BA_departure_num:
                    BA_trains_used += (BA_departure_num - extra_BA_trains)
                    extra_BA_trains = 0
                else:
                    extra_BA_trains -= BA_departure_num
            

        print "Case #%s:" % case_num, AB_trains_used, BA_trains_used

        case_num += 1
            
                    
def combine_train(string):
    train_timetable(arrange_train_message(train_transpose(string)))
    
    
        
        

