INPUT = {
    'data': ('int', 'linearray')
}

TEST = ('''\
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
''','''\
Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3
''')

def get_best(total):
    ''' returns best result given total, for both non-surprising and surprising case '''
    b, r = total / 3, total % 3
    if r == 0:
        if total > 0:
            return b, b + 1         # max score b, but surprising gives an extra point, if the score is at least 2
        else:
            return 0, 0
    elif r == 1:
        return b + 1, b + 1     # max score b + 1, and there can be no surprising combination
    elif r == 2:
       return b + 1, b + 2      # max score b + 1, suprising gives an extra point

def main(data):
    N, surprising, min_best = data[:3]
    totals = data[3:]
    
    count = 0
    
    for total in totals:
        best, best_with_surprising = get_best(total)
        
        if best >= min_best:
            count = count + 1
        elif surprising > 0 and best_with_surprising >= min_best:
            count = count + 1
            surprising = surprising - 1

    return count