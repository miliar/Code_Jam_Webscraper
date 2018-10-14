def main():
    with open('B-large.in', 'r') as f:
        rows = f.readlines()
        tests = int(rows[0])
        solutions = []
        for i in xrange(1, tests+1):
            S = rows[i].strip()
            L = len(S)
            counter = 0
            #print("**********************")
            #print(S)
            while counter < L:
                digit = int(S[counter])
                prev_digit = None
                next_digit = None
                left_satisfied = False
                right_satisfied = False
                if counter > 0:
                    prev_digit = int(S[counter-1])
                if counter < L-1:
                    next_digit = int(S[counter+1])
                if prev_digit == None or prev_digit <= digit:
                    left_satisfied = True
                if next_digit == None or digit <= next_digit:
                    right_satisfied = True
                if left_satisfied and right_satisfied:
                    counter += 1
                else:
                    #print("PRE CHANGE")
                    #print("S: " + S)
                    prev_digits = S[0:counter]
                    current_digit = str(digit-1)
                    next_digits = "9"*(L-counter-1)
                    S = prev_digits + current_digit + next_digits
                    #print("CHANGE")
                    #print("prev_digits: " + prev_digits)
                    #print("current_digit: " + current_digit)
                    #print("next_digits: " + next_digits)
                    #print("new S: " + S)
                    if(counter > 0):
                        counter -= 1
            S = S.lstrip("0")
            solutions.append(S)

        with open('B-large.out', 'w') as f:
            line_number = 1
            for line in solutions:
                f.write("Case #{0}: {1}\n".format(str(line_number), line))
                line_number += 1

main()
