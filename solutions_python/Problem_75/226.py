class LoopExit(BaseException):
    pass

def process(line):
    tokens = line.split(' ')
    num_combination = int(tokens.pop(0))
    combinations = dict()
    for i in range(0, num_combination):
        token = tokens.pop(0)
        bases = {}
        for element in token[0:-1]:
            bases[element] = bases.get(element, 0) + 1
        combinations[token[-1:]] = bases
    print combinations
    
    num_opposite = int(tokens.pop(0))
    opposites = set()
    for i in range(0, num_opposite):
        opposites.add(tokens.pop(0))
    print opposites   
    tokens.pop(0)
    sequence = tokens.pop(0)
    print sequence
    result = []
    for element in sequence:
        print element
        result.append(element)
        try:
            for start in range(len(result)-2, -1, -1):
                candidate = {}
                for cal in result[start:]:
                    candidate[cal] = candidate.get(cal, 0) + 1
                print candidate
                for key, value in combinations.items():
                    if value == candidate:
                        result = result[0:start]
                        result.append(key)
                        raise LoopExit
        except LoopExit:
            pass
        print result
        for peer in result[0:len(result)-1]:
            if result[-1]+peer in opposites or peer+result[-1] in opposites:
                result = []
                break
    print result
    return result


fin = open('B-small.in', 'r')
fout = open('B-small.out', 'w')
t = int(fin.readline().rstrip())
for i in range(1, t+1):
    line = fin.readline().rstrip()
    result = process(line)
    fout.write(('Case #%d: ['+', '.join(result)+']\n') % (i,))
    
fin.close()
fout.close()

