# helper functions

def tidy_number(n):
    digits = [int(x) for x in str(n)]
    max_digit = 0
    for i in digits:
        if (i >= max_digit):
            max_digit = i
        else:
            return False

    return True


def scale_down(N):
    digits = [int(x) for x in str(N)]
    new = []

    for i in range(0, len(digits), 1):
        if (i == len(digits)-1):
            new.append(str(digits[i]))
            break

        if(digits[i] <= digits[i+1]):
            new.append(str(digits[i]))
        else:
            new.append(str(digits[i]-1))
            for i in range(len(digits)-(i+1)):
                new.append('9')
            break

    return (int(''.join(new)))

def find_max(N):
    while(True):
        if(tidy_number(N)):
            return N
            break
        else:
            N = scale_down(N)


# input and output
examples_no = int(input()) # number of instances
for i in range(1, examples_no+1):
    n = int(input())  # input integer
    print("Case #{}: {}".format(i, find_max(n)))
    # check out .format's specification for more formatting options
