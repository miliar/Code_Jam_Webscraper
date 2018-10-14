def is_line_happy(s):
    return s == '+' * len(s)
    
def get_first_blank(s):
    return s.find('-')

def flip_single_pancake(i):
    return '+' if i == '-' else '-'
    
def flip_pancakes(s, k ,index):
    result = ''
    for i in range(len(s)):
        if index <= i < index + k:
            result += flip_single_pancake(s[i])
        else:
            result += s[i]
    return result
    
def operate(s, k):
    tries = 0
    while not is_line_happy(s):
        first_blank = get_first_blank(s)
        if first_blank > len(s) - k:
            return 'IMPOSSIBLE'
        s = flip_pancakes(s, k, first_blank)
        tries += 1
    return tries
    
def parse_input():
    T = int(raw_input())
    for i in range(1, T+1):
        s, k = raw_input().split(' ')
        print "Case #{0}: {1}".format(i, str(operate(s, int(k))))
        
parse_input()
