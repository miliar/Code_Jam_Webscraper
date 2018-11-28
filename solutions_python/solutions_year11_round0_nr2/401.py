'''
Created on 7-may-2011

@author: Joachim Van Herwegen
'''

def parse_line(line):
    parts = line.split()
    total_combinations = int(parts.pop(0))
    combinations = {}
    for i in xrange(total_combinations):
        combination = parts.pop(0)
        input = combination[0:2]
        output = combination[2]
        combinations[input] = output
        combinations[input[::-1]] = output
    
    total_opposing = int(parts.pop(0))
    opposing = {}
    for i in xrange(total_opposing):
        opp = parts.pop(0)
        for j in xrange(2):
            if not opp[j] in opposing:
                opposing[opp[j]] = set()
            opposing[opp[j]].add(opp[j-1])
    
    return combinations, opposing, list(parts[1])

def calc_result(combinations, opposing, sequence):
    result = []
    
    while sequence:
        next = sequence.pop(0)
        if result and result[-1]+next in combinations:
            combination = combinations[result[-1]+next]
            if combination:
                result[-1] = combination
                continue
        if next in opposing:
            if set(result).intersection(opposing[next]):
                result = []
                continue
        result.append(next)
    return result

def result_to_str(input):
    result = '['
    for i in xrange(len(input)):
        result += input[i]
        if i < len(input)-1:
            result += ', '
    result += ']'
    return result

def main():
    file = open("magicka_large.txt", 'rU')
    file.readline()
    results = []
    for line in file:
        c,o,s = parse_line(line)
        results.append(result_to_str(calc_result(c,o,s)))
    file.close()
    
    output = open("output_magicka_large.txt", 'w')
    for i, result in enumerate(results):
        output.write("Case #%d: %s" % (i+1, str(result)))
        if i < len(results)-1:
            output.write("\n")
    output.close()

if __name__ == "__main__":
    main()