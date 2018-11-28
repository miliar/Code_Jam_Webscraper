import sys

root = 'C:\\Users\\davedave\\Downloads'
problemLetter = 'B'
infile = '{}\\{}-{}.in'.format(root, problemLetter, 'large')
#infile = '{}\\test.in'.format(root)
outfile = infile.replace('.in', '.out')


def get_prob(roles, probabilities):
    p = 1
    for i in range(roles):
        p *= 1 - probabilities[i] * probabilities[len(probabilities) - 1 - i]
    return p


def is_tidy_num(curr):
    currString = str(curr)
    sortedCurrString = ''.join(sorted(currString))
    return currString == sortedCurrString


def construct_last_tidy_num(curr):
    if is_tidy_num(curr):
        return curr

    digitList = [int(d) for d in str(curr)]

    i = 1
    while i < len(digitList):
        if digitList[i] < digitList[i-1]:
            # decrement digit at i by 1
            digitList[i-1] -= 1
            # set all digits after i to 9
            j = i
            while j < len(digitList):
                digitList[j] = 9
                j+=1
            return construct_last_tidy_num(convert_digit_list_to_int(digitList))
        i+=1

def convert_digit_list_to_int(digitList):
    return int(''.join(map(str, digitList)).lstrip('0'))

if __name__ == '__main__':
    with open(infile, 'r') as fin, open(outfile, 'w') as fout:
        for case in range(int(fin.readline())):
            curr = int(fin.readline())
            if curr <= 19 or is_tidy_num(curr):
                last_tidy = curr
            else:
                last_tidy = construct_last_tidy_num(curr)
            msg = 'Case #{}: {}'.format(1+case, last_tidy)
            print(msg)
            fout.write(msg + '\n')
