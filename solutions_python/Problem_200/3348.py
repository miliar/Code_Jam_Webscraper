import fileinput

def flip_with_flipper(S, k, index):
    for i in xrange(k):
        if S[index + i] == "-":
            S[index + i] = "+"
        else:
            S[index + i] = "-"

def solve(k):
    answer = ""
    repeat_count = 1 # Used for counting how much back update I need in case of lower digit

    len_k = len(k)
    is_breaked = False

    if len_k == 1:
        return k

    for i in xrange(len_k - 1):
        current_digit = k[i]
        next_digit = k[i+1]

        if  current_digit == next_digit:
            # Increase repeat_count - to remmmber back
            repeat_count += 1
        elif current_digit > next_digit:
            digit_to_insert = chr(ord(current_digit) - 1)
            new_string = digit_to_insert
            new_string += "9" * (repeat_count - 1)
            
            if len(answer) == 0 and digit_to_insert == "0":
                repeat_count -= 1
                new_string = "9" * repeat_count

            answer += new_string

            # Now - all last digits can be 9
            leftover_count = len_k - 1 - i
            answer += "9" * leftover_count

            is_breaked = True
            break
        else:
            #Found explicty larger difit - we dont need to back remmember
            new_string = current_digit * repeat_count
            answer += new_string

            repeat_count = 1

    # Fill leftovers
    if is_breaked == False and repeat_count > 1:
        answer += current_digit * repeat_count
    # Fill leftovers - last number
    elif is_breaked == False:
        answer += next_digit

    return answer.lstrip("0")

if __name__ == "__main__":
    f = fileinput.input()

    T = int(f.readline()) # Number of cases
    for case in xrange(1, T + 1):
        k = f.readline()
        solution = solve(k.strip())
        print("Case #{0}: {1}".format(case, solution))