def validate(text):
    if len(text) == 0:
        return True
    current = text[0]
    seen = set([current])
    for c in text[1:]:
        if c != current:
            if c in seen:
                return False
            seen.add(c)
            current = c
    return True


def validate_all(cars):
    for subtrain in cars:
        if not validate(subtrain):
            return False
    return True


def is_one_letter(car):
    return car[0] == car[-1]


def remove_duplicate_elements(cars):
    count = {}
    for c in cars:
        count[c] = count.get(c, 0) + 1
        if count[c] > 1 and not is_one_letter(c):
            # We don't allow duplicate elements that are not formed of 1 letter
            return False
    return [(v * k, v) for k, v in count.items()]


def group_gy_first_letter(cars):
    cars_by_first = {}
    for car, count in cars:
        first = car[0]
        if first in cars_by_first:
            previous_car, previous_count = cars_by_first[first]
            if is_one_letter(car):
                cars_by_first[first] = car + \
                    previous_car, count * previous_count
            elif is_one_letter(previous_car):
                cars_by_first[first] = previous_car + \
                    car, count * previous_count
            else:
                return False
        else:
            cars_by_first[first] = car, count
    for car, count in cars_by_first.values():
        if is_one_letter(car):
            first = car[0]
            cars_by_first[first] = car, fact(count)

    return cars_by_first


def link_cars(cars_by_first):
    cars = cars_by_first.values()
    while(cars):
        current, count = cars.pop()
        last = current[-1]
        first = current[0]
        if first in cars_by_first:
            if last in cars_by_first and first != last:
                next, next_count = cars_by_first[last]
                cars_by_first[first] = (current + next, count * next_count)
                cars.append(cars_by_first[first])
                del cars_by_first[last]
    return cars_by_first.values()


def mult_modulo(m, n):
    return (m * n) % 1000000007


def remove_one_letters(cars):
    return [c[0] if is_one_letter(c) else c for c in cars]


def fact(l):
    return reduce(mult_modulo, xrange(1, l + 1))


def count(cars):
    # for a train to be valid, all elements in the set should also be valid
    # trains
    if not validate_all(cars):
        return 0
    if len(cars) == 1:
        return 1
    cars_without_one_letter = remove_one_letters(cars)
    # remove duplicate elements
    cars_without_duplicates = remove_duplicate_elements(cars_without_one_letter)
    if not cars_without_duplicates:
        return 0
    # group element by first letteer
    cars_by_first = group_gy_first_letter(cars_without_duplicates)
    if not cars_by_first:
        return 0
    # Link elements together
    linked_cars = link_cars(cars_by_first)
    words = [current for current, count in linked_cars]
    print [(x[0], x[-1], count) for x, count in linked_cars]
    # now, we should be able to put all elements together in any position
    if not validate(''.join(words)):
        return 0

    n_permutations = fact(len(linked_cars))
    counts = [count for current, count in linked_cars]
    counts.append(n_permutations)
    return reduce(mult_modulo, counts)


if __name__ == '__main__':
    with open('test.txt') as instream:
        with open('result.txt', 'w') as outstream:
            t = int(instream.readline())
            for c in xrange(t):
                    n = int(instream.readline())
                    cars = instream.readline().strip().split(' ')
                    if c > -1:
                        print c, [(x[0], x[-1]) for x in cars]
                        cars_by_first = count(cars)
                        outstream.write("Case #{}: {}\n".format(
                            c + 1, cars_by_first))
