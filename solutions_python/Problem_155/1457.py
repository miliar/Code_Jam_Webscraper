cases = int(raw_input())
for case in range(1, cases+1):
    max_t, t_array = raw_input().split(" ")
    number_of_people = 0
    number_to_add = 0
    for i, num in enumerate(t_array):
        num = int(num)
        if number_of_people < i:
            temp_number_to_add = i - number_of_people
            number_to_add += temp_number_to_add
            number_of_people += temp_number_to_add
        number_of_people += num
    print("Case #%s: %s" % (case, number_to_add))