from sys import stdin, stderr, stdout

def read_line():
    return stdin.readline().rstrip('\r\n')

def read_ints():
    line = read_line()
    return map(int,
               line.rstrip('\r\n').split(' '))

def get_bigger(list, number):
    ind = 0
    while ind < len(list) and list[ind] <= number:
        ind += 1
    if ind < len(list):
        return list[ind:]
    return []


def solve_case(number):
    # maximal of length
    max_of_length = True
    for i in range(1, len(number)):
        if number[i-1] < number[i]:
            max_of_length = False
            break

    if max_of_length:
        #print >> stderr, "max", number
        if len(number) == 1:
            new_number = [number[0], '0']
            return new_number

        # add 0 and construct the smallest
        new_number = ['0'] + number
        new_number.sort()
        #print >> stderr, "sorted:", new_number
        i = 0
        while new_number[i] == '0':
            #print >> stderr, "found 0 in index", i
            i += 1
        # swap new_number[i] and new_number[0]
        temp = new_number[0]
        new_number[0] = new_number[i]
        new_number[i] = temp


        return new_number


    else:
        sorted = [] + number
        sorted.sort()
        #print >> stderr, "sorted", sorted

        for i in range(len(number)-1, -1, -1):
            #print >> stderr, "can we move number", i, number[i]
            # what are the bigger numbers?
            bigger = get_bigger(sorted, number[i])
            #print >> stderr, "bigger:", bigger
            behind = []
            if i < len(number)-1:
                behind = number[(i+1):]
            #print >> stderr, "behind:", behind
            candidates = list(set(behind).intersection(set(bigger)))
            if len(candidates) > 0:
                #print >> stderr, "we can"
                candidates.sort()
                new_number = [] + number
                new_number[i] = candidates[0]
                if i < len(number)-1:
                    rest_numbers = number[i:]
                    rest_numbers.remove(candidates[0])
                    rest_numbers.sort()
                    new_number[(i+1):] = rest_numbers
                #print >> stderr, "new: ", new_number
                return new_number

if __name__ == '__main__':
    no_cases = read_ints()[0]
    print >> stderr, "No of cases: %d" % no_cases
    for case in xrange(no_cases):
        number_str = list(read_line())
        print >> stderr, "Solving case %d" % (case + 1)
        #print >> stderr, "%s" % (number_str)

        next = solve_case(number_str)
        stdout.write("Case #%d: " % (case + 1))
        for s in next:
            stdout.write('%s' % s)
        stdout.write("\n")
