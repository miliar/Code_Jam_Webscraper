import re
import pdb

def debug_print(items):
    result = ''
    for item in items:
        result += str(item) + ' '
    print result

file = open('B-large.in')
source = file.read().split('\n')
file.close()

number_testcases = int(source[0])
test_cases = source[1:-1]

results = ''
case_number = 1
for case in test_cases:

    _combine = re.search('\d+ [A-Z\s]*\d', case).group()[:-2]
    _series = case[len(_combine)+1:]
    _oppose = re.search('\d+ [A-Z\s]*\d', _series).group()[:-2]
    _series = _series[len(_oppose)+1:]

    c = re.search('\d+', _combine).group()
    __combine = re.findall('[A-Z]{3}', _combine)
    d = re.search('\d+', _oppose).group()
    __oppose = re.findall('[A-Z]{2}', _oppose)
    n = re.search('\d+', _series).group()
    __series = re.findall('[A-Z]', _series)

    combine = {}
    for case in __combine:
        combine[(case[0:1], case[1:2])] = case[2:3]
        combine[(case[1:2], case[0:1])] = case[2:3]
    oppose = {} 

    for case in __oppose:
        if case[0:1] in oppose:
            oppose[case[0:1]].append(case[1:2])
        else:
            oppose[case[0:1]] = [case[1:2]]
        if case[1:2] in oppose:
            oppose[case[1:2]].append(case[0:1])
        else:
            oppose[case[1:2]] = [case[0:1]]
    series = __series

    elements = []
    
    for element in series:
        #pdb.set_trace()
        if not elements:
            elements.append(element)
        else:
            last = elements[-1]
            if combine.has_key((element, last)):
                elements.pop()
                elements.append(combine[(element, last)])
            elif element in oppose and set(oppose[element]) & set(elements):
                elements = []
            else:
                elements.append(element)

    
    results += "Case #" + str(case_number) + ": ["
    if elements:
        for element in elements:
            results += element + ', '
        results = results[:-2] + ']'
    else:
        results += ']'
    if case_number != number_testcases:
       results += '\n'
    case_number += 1

print results

out = open('results.out', 'w')
out.write(results)
out.close()

