
def multiply(o1, o2):
    sign = ''
    if(('-' in o1 and '-' not in o2) or
       ('-' in o2 and '-' not in o1)):
        sign = '-'
    x = o1.replace('-', '')
    y = o2.replace('-', '')
    if x == 'i':
        if y == 'i':
            result = '-1'
        elif y == 'j':
            result = 'k'
        elif y == 'k':
            result = '-j'
        else:
            result = x
    elif x == 'j':
        if y == 'i':
            result = '-k'
        elif y == 'j':
            result = '-1'
        elif y == 'k':
            result = 'i'
        else:
            result = x
    elif x == 'k':
        if y == 'i':
            result = 'j'
        elif y == 'j':
            result = '-i'
        elif y == 'k':
            result = '-1'
        else:
            result = x
    elif x == '1':
        if y == 'i':
            result = 'i'
        elif y == 'j':
            result = 'j'
        elif y == 'k':
            result = 'k'
        else:
            result = x

    if sign == '-':
        if '-' == result[0]:
            return result[1:]
        else:
            return '-' + result
    return result


def calculate(input_str, result_letter):
    result = input_str[0]
    for i, letter in enumerate(input_str[1:]):
        result = multiply(result, letter)
        if result_letter != 'k':
            if result == result_letter:
                return True, input_str[i+2:]
    if result_letter == 'k':
        if result == result_letter:
            return True, ''
    return False, ''



def solve(L, X, search_str):
    if L*X < 3:
        return 'NO'
    elif search_str == 'ijk':
        return 'YES'

    found, sub_str_j = calculate(search_str, 'i')
    if found:
        found, sub_str_k = calculate(sub_str_j, 'j')
        if found:
            if sub_str_k == 'k':
                return 'YES'
            found, sub_str_end = calculate(sub_str_k, 'k')
            if found:
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    testcases = input()

    for caseNr in range(1, int(testcases)+1):
        L, X = input().split(' ')
        str_to_repeat = input()
        print("Case #%i: %s" % (caseNr, solve(int(L), int(X), str_to_repeat*int(X))))