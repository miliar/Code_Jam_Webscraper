
def is_tidy(number):
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            return False
    return True

def lowest_tidy_index(number):
    for i in range(len(number)-1, -1, -1):
        if number[i] < number[i-1]:
            return i
    return 0

def reduce_jump(number, lti):
    suffix = '9' * (len(number) - lti)
    p = int(number[:lti]) -1
    prefix = str(p) if p > 0 else ''
    return prefix + suffix

def make_tidy(number):
    lti = lowest_tidy_index(number)
    while lti != 0:
        number = reduce_jump(number, lti)
        lti = lowest_tidy_index(number)
    return number

T = int(input())
for c in range(1, T+1):
    print('Case #{}: {}'.format(c, make_tidy(input().strip())))


