table = {
    '1': {
        '1': {'value': '1', 'neg_flag': 1}, 
        'i': {'value': 'i', 'neg_flag': 1}, 
        'j': {'value': 'j', 'neg_flag': 1}, 
        'k': {'value': 'k', 'neg_flag': 1}, 
    },
    'i': {
        '1': {'value': 'i', 'neg_flag': 1}, 
        'i': {'value': '1', 'neg_flag': -1}, 
        'j': {'value': 'k', 'neg_flag': 1}, 
        'k': {'value': 'j', 'neg_flag': -1}, 
    },
    'j': {
        '1': {'value': 'j', 'neg_flag': 1}, 
        'i': {'value': 'k', 'neg_flag': -1}, 
        'j': {'value': '1', 'neg_flag': -1}, 
        'k': {'value': 'i', 'neg_flag': 1}, 
    },
    'k': {
        '1': {'value': 'k', 'neg_flag': 1}, 
        'i': {'value': 'j', 'neg_flag': 1}, 
        'j': {'value': 'i', 'neg_flag': -1}, 
        'k': {'value': '1', 'neg_flag': -1}, 
    }
}


def find(ijk, find_letter): 
    neg_flag = 1
    current_letter = '1'
    for i, letter in enumerate(ijk): 
        result = table[current_letter][letter]
        current_letter = result['value']
        neg_flag *= result['neg_flag']
        if current_letter == find_letter: 
            return i, neg_flag
    return None
        
def multiply_all(ijk): 
    neg_flag = 1
    current_letter = '1'
    for letter in ijk: 
        result = table[current_letter][letter]
        current_letter = result['value']
        neg_flag *= result['neg_flag']
    return current_letter, neg_flag
    

def dijkstra(ijk): 
    neg_flag = 1
    result = find(ijk, 'i')
    if not result: 
        return 'NO'
    pos, flag1 = result
    ijk = ijk[pos+1:]
    result = find(ijk, 'j')
    if not result: 
        return 'NO'
    pos, flag2 = result
    ijk = ijk[pos+1:]
    result = find(ijk, 'k')
    if not result: 
        return 'NO'
    pos, flag3 = result
    ijk = ijk[pos+1:]
    letter, flag4 = multiply_all(ijk)
    if letter != '1': 
        return 'NO'
    if flag1*flag2*flag3*flag4 != 1: 
        return 'NO'
    return 'YES'
    
if __name__ == '__main__': 
    num_tests = int(raw_input())
    for i in range(num_tests): 
        _, repetitions = raw_input().strip().split()
        l = raw_input().strip()
        ijk = [x for x in l*int(repetitions)]
        print('Case #%d: %s' % (i+1, dijkstra(ijk)))