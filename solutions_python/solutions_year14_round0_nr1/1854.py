def convert_to_array(x):
    lst = x.split()
    lst = [int(a) for a in lst]
    return lst
total = input()
m =0 
answer_list = []
while m < total:
	first_answer = input()

	first_first = raw_input()
	first_second = raw_input()
	first_third = raw_input()
	first_fourth = raw_input()

	second_answer = input()

	second_first = raw_input()
	second_second = raw_input()
	second_third = raw_input()
	second_fourth = raw_input()

	first_deck = []
	first_deck.append(convert_to_array(first_first))
	first_deck.append(convert_to_array(first_second))
	first_deck.append(convert_to_array(first_third))
	first_deck.append(convert_to_array(first_fourth))

	second_deck =[]
	second_deck.append(convert_to_array(second_first))
	second_deck.append(convert_to_array(second_second))
	second_deck.append(convert_to_array(second_third))
	second_deck.append(convert_to_array(second_fourth))

	lst1 = first_deck[first_answer - 1]
	lst2 = second_deck[second_answer - 1]
	check=0
	mark =0
	for i in lst1:
		for j in lst2:
			if i==j:
			    	answer = i
				mark = 1
				if  check == 0:
					check+=1
				else:
					mark = 2
					break
		if mark ==2:
			break

	if mark == 0:
		answer_list.append("Volunteer cheated!")
	elif mark == 1:
		answer_list.append(answer)
	elif mark == 2:
		answer_list.append("Bad magician!")
	m+=1
i=0
while i<total:
    print "Case"+" #"+str(i+1)+": "+str(answer_list[i])
    i+=1
