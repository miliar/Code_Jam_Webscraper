def main():
    for case in range(input()):
        digit_used = [False for i in range(36)]
        used_digit = {}
        max_digit = 0
        alian_string = raw_input()
        alian_numbers = []
        for index in range(len(alian_string)):
            alian_charactor = alian_string[index]
            if used_digit.has_key(alian_charactor):
                alian_numbers.append(used_digit[alian_charactor])
            else:
                if index == 0:
                    next_digit = 1
                else:
                    next_digit = 0
                    for i in range(36):
                        if not digit_used[i]:
                            next_digit = i
                            break
                used_digit[alian_charactor] = next_digit
                digit_used[next_digit] = True
                alian_numbers.append(next_digit)
                if next_digit > max_digit:
                    max_digit = next_digit
        max_digit += 1
#        print alian_numbers, max_digit
        min_seconds = 0
        for digit in alian_numbers:
            min_seconds = min_seconds * max_digit + digit
        print "Case #%d: %d" % (case + 1, min_seconds)
        
main()
