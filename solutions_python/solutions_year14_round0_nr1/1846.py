def string_to_array(x):
    input_list = x.split()
    input_list = [int(a) for a in input_list]
    return input_list
cases = input()
m =0 
answer_list = []
while m <cases:
    first_answer = input()
    first_first_row = raw_input()
    first_second_row = raw_input()
    first_third_row = raw_input()
    first_fourth_row = raw_input()
    second_answer = input()
    second_first_row = raw_input()
    second_second_row = raw_input()
    second_third_row = raw_input()
    second_fourth_row = raw_input()
    
    first_deck = []
    first_deck.append(string_to_array(first_first_row))
    first_deck.append(string_to_array(first_second_row))
    first_deck.append(string_to_array(first_third_row))
    first_deck.append(string_to_array(first_fourth_row))
    
    second_deck =[]
    second_deck.append(string_to_array(second_first_row))
    second_deck.append(string_to_array(second_second_row))
    second_deck.append(string_to_array(second_third_row))
    second_deck.append(string_to_array(second_fourth_row))
    
    lst1 = first_deck[first_answer - 1]
    lst2 = second_deck[second_answer - 1]
    count=0
    check =0
    for i in lst1:
        for j in lst2:
            if i==j:
                ans = i
                check = 1
                if  count == 0:
                    count+=1
                else:
                    check = 2
    
    if check == 1:
        answer_list.append(ans)
    elif check == 0:
        answer_list.append("Volunteer cheated!")
    elif check == 2:
        answer_list.append("Bad magician!")
    m+=1
i=0
while i<cases:
    string = "Case #"+(str)(i+1)+":"+" "+(str)(answer_list[i])
    print string
    i+=1
