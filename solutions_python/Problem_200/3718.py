__author__ = 'whiterock'


def is_tidy(n):
    if n % 10 == 0:
        return False
    else:
        return list(str(n)) == sorted(list(str(n)))


with open('tidynumbers_test.txt') as input_file:
    lines = input_file.readlines()
    print '#', lines[0]
    for i, case in enumerate(lines[1:]):
        sample = int(case.strip())
        n = sample
        while True:

            if is_tidy(n):
                print "Case #{}: {}".format(i+1, n)
                break

            previous_place = 0
            for c, place in enumerate(str(n)):
                if int(place) < previous_place:
                    length = len(str(n))
                    new_n = "{}{}{}".format(str(n)[:c-1], previous_place-1, '9'*(length-c))
                    #print ">", n
                    #print int(place), "is smaller than", previous_place, "@", c+1
                    #print "=", new_n
                    n = int(new_n)
                    break

                previous_place = int(place)

            if is_tidy(n):
                print "Case #{}: {}".format(i+1, n)
                break

            n -= 1