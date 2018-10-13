import sys

def main():
    total = int(sys.stdin.readline())
    for i in range(total):
        line = sys.stdin.readline()
        state, k = line.rstrip().split(' ')
        result = find_flips(state, int(k))
        print ('Case #{}: {}'.format(i + 1, result))

def find_flips(state, k):
    state = list(map(lambda x: True if (x == '+') else False, state))
    i = 0
    length = len(state)
    reverse = 0
    
    flip = 0
    while i < length:
        if not state[i]:
            reverse += 1
            if reverse == k:
                flip += 1
                reverse = 0
                
        elif reverse > 0:
            if (i + k) > length:
                break
            else:
                state[i: i + k] = list(map(lambda x: not x, state[i: i + k]))
                flip += 1
                i -= 1
        i += 1
    
    if reverse > 0:
        return 'IMPOSSIBLE'
    
    return flip
        
if __name__ == '__main__':
    main()