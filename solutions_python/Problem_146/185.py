import sys

#f_in = open("B-large.in", "r")
f_in = open("B-small-attempt1.in", "r")
#f_in = open("train.in", "r")
f_out = open("train.out", "w")

size = int(f_in.readline())

def can_connect(car1, car2):
    return car1[-1] == car2[0]

def car_valid(car):
    current = ""
    done_letters = set([])
    for letter in car:
        if letter in done_letters:
            return False
        if current == "":
            current = letter
        elif letter != current:
            done_letters.add(current)
            current = letter

    return True

def shorten(car):
    current = ""
    result = ""
    for letter in car:
        if current == "":
            current = letter
        elif letter != current:
            result += current
            current = letter

    result += current

    return result

def count_trains(car, all_cars, cars_lookup, available_cars, cars_left):
    if cars_left == 0:
        return 1

    total = 0
    for letter_i in range(len(car)):
        if letter_i < len(car) - 1 and car[letter_i + 1] != car[letter_i]:
            candidates = cars_lookup[car[letter_i]]
            for candidate in candidates:
                if available_cars[candidate] > 0:
                    return 0 # the following letter blocks off connection to current

    candidates_temp = set(cars_lookup[car[-1]])
    candidates = []
    for candidate in candidates_temp:
        candidates += [candidate] * available_cars[candidate]

    #print candidates

    found_unused = False
    if len(candidates) > 0:
        for candidate in candidates:
            if car[-1] in candidate and not candidate[0] == car[-1] and available_cars[candidate] > 0:
                return 0
            if candidate[0] == car[-1] and available_cars[candidate] > 0:
                found_unused = True
                available_cars[candidate] -= 1
                total += count_trains(candidate, all_cars, cars_lookup, available_cars, cars_left - 1)
                available_cars[candidate] += 1
    
    if not found_unused:
        for car in all_cars:
            if available_cars[car] > 0:
                available_cars[car] -= 1
                total += count_trains(car, all_cars, cars_lookup, available_cars, cars_left - 1)
                available_cars[car] += 1

    return total

for case_num in range(size):
    print "case " + str(case_num)
    train_size = int(f_in.readline().strip())
    all_cars = [x for x in f_in.readline().strip().split()]
    available_cars = {}
    cars = {}

    shortened = []
    for car in all_cars:
        shortened.append(shorten(car))

    all_cars = shortened
    print all_cars

    for car in all_cars:
        if car not in available_cars:
            available_cars[car] = 0
        available_cars[car] += 1

        for letter in car:
            if letter not in cars:
                cars[letter] = set([])
            cars[letter].add(car)

    total = 0
    for car in all_cars:
        if car_valid(car):
            available_cars[car] -= 1
            total += count_trains(car, all_cars, cars, available_cars, len(all_cars) - 1)
            available_cars[car] += 1
        else:
            total = 0
            break

    f_out.write("Case #" + str(case_num + 1) + ": " + str(total % 1000000007) + "\n")

f_in.close()
f_out.close()