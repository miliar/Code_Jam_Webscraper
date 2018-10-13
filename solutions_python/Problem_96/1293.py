f = open('input', 'r')
f.readline()
cases = []
for l in f:
    case = {}
    l = l.split(' ')
    case['surprises'] = int(l[1])
    case['p'] = int(l[2])
    case['scores'] = []
    for n in l[3:]:
        case['scores'].append(int(n))
    cases.append(case)
        
def answer(case):
    if case['p'] >= 2:
        lowest_score = case['p'] + 2*(case['p']-1)
        lowest_score_with_surprise = case['p'] + 2*(case['p']-2)
    elif case['p'] == 1:
        lowest_score = case['p'] + 2*(case['p']-1)
        lowest_score_with_surprise = case['p'] + 2*(case['p']-1)
    elif case['p'] == 0:
        lowest_score = case['p'] + 2*(case['p'])
        lowest_score_with_surprise = case['p'] + 2*(case['p'])
    
    result = 0
    surprises = case['surprises']
    for score in case['scores']:
        if score >= lowest_score:
            result += 1
        elif score >= lowest_score_with_surprise and surprises > 0:
            result += 1
            surprises -= 1
    return result

out = open('output', 'w')
i=1
for case in cases:
    out.write("Case #%d: %s\n" % (i, answer(case)))
    i += 1