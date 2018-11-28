import math

def is_palindrome(number):
    str_number = str(number)

    if len(str_number) > 1:
        for i in xrange(int(math.ceil(len(str_number) / 2))):
            if str_number[i] != str_number[-1]:
                return False

    return True

def print_results(results):
    for i in range(len(results)):
        print 'Case #' + str(i + 1) + ": " + str(results[i])

def main():
    results = []
    memoization = {}

    cases = int(raw_input())

    for i in xrange(cases):
        num_fair_square = 0
        limits_range = raw_input().split(" ")

        min_limit = int(limits_range[0])
        max_limit = int(limits_range[1])

        sqrt_min_in_range = int(math.ceil(math.sqrt(min_limit)))
        sqrt_max_in_range = int(math.floor(math.sqrt(max_limit)))

        for number in xrange(sqrt_min_in_range, sqrt_max_in_range + 1):
            if is_palindrome(number):
                square = number*number

                if square in memoization:
                    if memoization[square]:
                        num_fair_square += 1
                else:
                    if is_palindrome(square):
                        memoization[square] = True
                        num_fair_square += 1
                    else:
                        memoization[square] = False

        results.append(num_fair_square)

    print_results(results)



if __name__ == "__main__":
    main()
