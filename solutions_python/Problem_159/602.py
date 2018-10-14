__author__ = 'Nikola Culumovic'

number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    number_of_shrooms = int(input())
    plate = str(input()).split()
    method_1 = 0
    method_2 = 0
    method_2_speed = 0
    plate[0] = int(plate[0])
    for j in range(number_of_shrooms - 1):
        plate[j+1] = int(plate[j+1])
        if plate[j+1] < plate[j]:
            delta = plate[j] - plate[j+1]
            method_1 += delta
            if delta > method_2_speed:
                method_2_speed = delta
    for j in range(number_of_shrooms-1):
        if plate[j] < method_2_speed:
            method_2 += plate[j]
        else:
            method_2 += method_2_speed

    print("Case #"+str(i+1)+": "+str(method_1)+" "+str(method_2))

