filename = 'large'

def create_combinations(tokens):
    result = {}
    
    for combination in tokens:
        key = [combination[0], combination[1]]
        key.sort()
        key = ''.join(key)
        if not result.has_key(key):
            result[key] = combination[2]
    
    return result

def create_opposeds(tokens):
    result = []
    
    for opposition in tokens:
        key = [opposition[0], opposition[1]]
        key.sort()
        key = ''.join(key)
        if not key in result:
            result.append(key)
    
    return result

def invoke(elements, combinations, opposeds):
    result = []
    
    for e in elements:
        result.append(e)
        if len(result) == 1:
            continue
        tmp = [result[-2], e]
        tmp.sort()
        tmp = ''.join(tmp)
        if combinations.has_key(tmp):
            result.pop()
            result.pop()
            result.append(combinations[tmp])
            continue
        for r in result[:-1]:
            tmp = [r, e]
            tmp.sort()
            tmp = ''.join(tmp)
            if tmp in opposeds:
                result = []
    
    return result

def solve(tokens):
    qtd_combinations = int(tokens.pop(0))
    combinations = {}
    if qtd_combinations > 0:
        tmp = tokens[:qtd_combinations]
        tokens = tokens[qtd_combinations:]
        combinations = create_combinations(tmp)
    
    qtd_opposeds = int(tokens.pop(0))
    opposeds = []
    if qtd_opposeds > 0:
        tmp = tokens[:qtd_opposeds]
        tokens = tokens[qtd_opposeds:]
        opposeds = create_opposeds(tmp)
    
    qtd_invokeds = int(tokens.pop(0))
    result = []
    if qtd_invokeds > 0:
        result = invoke(tokens.pop(0), combinations, opposeds)
    
    return result

def main():
    file_in = open('B-%s.in' % filename)
    file_out = open('B-%s.out' % filename, 'w')
    cases = int(file_in.readline().strip())
    for case in xrange(1, cases + 1):
        result = solve(file_in.readline().strip().split(' '))
        file_out.write('Case #%d: %s\n' % (case, str(result).replace('\'', '')))
    file_out.close()
    file_in.close()
    return

if __name__ == '__main__':
    main()
    import sys
    sys.exit(0)
