test_cases = int(input())
for i in range(test_cases):
    people_cnt, shyness_arr =  str(input()).split()
    people_cnt, total_people_attended, people_needed = int(people_cnt), int(shyness_arr[0]), 0
    for shyness_level in range(1, people_cnt + 1):
        new_people = 0
        if shyness_level > total_people_attended:
            new_people = shyness_level -total_people_attended
            people_needed += shyness_level-total_people_attended
        total_people_attended += int(shyness_arr[shyness_level]) + new_people
        
    print('Case #{}: {}'.format(i+1, people_needed))