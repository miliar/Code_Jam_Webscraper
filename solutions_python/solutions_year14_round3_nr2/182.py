from collections import defaultdict
from time import time

f_in = open('input2.txt')
f_out = open('output2.txt', 'w')
t = int(f_in.readline())

def read(f_in):
    f_in.readline()
    cars = f_in.readline().split()

    mod_cars = []
    for car in cars:
        prev_letter = None
        count = 0
        mod_car = []
        for letter in car:
            if prev_letter and prev_letter != letter:
                mod_car.append((prev_letter, count))
                count = 0
            count += 1
            prev_letter = letter
        mod_car.append((prev_letter, count))
        mod_cars.append(mod_car)
    return cars, mod_cars

def count_letters(cars):
    counts = defaultdict(int)
    for car in cars:
        for letter in car:
            counts[letter] += 1
    return counts

def count_while_ok(car_ids, mod_cars, counts):
    count = 0
    prev_letter = None
    for car_id in car_ids:
        for letter, letter_cnt in mod_cars[car_id]:
            if prev_letter and prev_letter != letter:
                if counts[prev_letter] != count:
                    return False
                count = 0
            count += letter_cnt
            prev_letter = letter
    return True

def solve(used_ids, mod_cars, counts):
    if not count_while_ok(used_ids, mod_cars, counts):
        return 0
    if len(used_ids) == len(mod_cars):
        return 1

    found = 0
    for i in range(len(mod_cars)):
        if i not in used_ids:
            found += solve(used_ids + [i], mod_cars, counts)
    return found

a = time()
for testcase in range(t):
    print "."
    cars, mod_cars = read(f_in)
    counts = count_letters(cars)
    answer = solve([], mod_cars, counts)
    f_out.write('Case #{0}: {1}\n'.format(testcase + 1, answer))

f_out.close()
print time() - a
