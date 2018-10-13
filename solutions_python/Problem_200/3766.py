def is_non_decreasing(number):
    number_str = str(number)
    last_seen = number_str[0]
    seen_numbers = 1
    for n in number_str[1:]:
        if n < last_seen:
            jump_length = int(number_str[seen_numbers:])
            #print("jumping by: %s" % jump_length)
            number -= jump_length
            return (number, False)
        seen_numbers += 1
        last_seen = n
    return (number, True)

def last_tidy_number(N):
    # return last tidy number before N
    number = N
    while number >= 0:
        number, res = is_non_decreasing(number)
        if res:
            return number
        number -= 1
    return number

def main():
    with open('/Users/alex/Downloads/B-large.in.txt', 'r') as f:
        nCases = int(f.readline())
        for n in range(nCases):
            N = int(f.readline())
            result = last_tidy_number(N)
            print 'Case #%s: %s' % (str(n+1), str(result))

if __name__ == '__main__':
    main()
