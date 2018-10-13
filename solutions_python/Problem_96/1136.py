import math

file = 'B-large'

#Input
with open(file + '.in', 'r') as input:
    T = int(input.readline())
    cases = []
    for line in input.readlines():
        numbers = map(int, line.split(' '))
        cases.append({
            'surprise': numbers[1],  # number of surprising triplets
            'min_score': numbers[2],  # best result to check for gte
            'scores': numbers[3:], # N total points of googlers
        })

# Processing

# Set up the scores as equal
for i, case in enumerate(cases):
    case['above_min_score'] = 0
    case['surprise_rem'] = case['surprise']

    for j, score in enumerate(case['scores']):
        # Setup a base score
        s = math.floor(score/3)
        case['scores'][j] = {
                'total': score,
                'scores': [s]*3
                }

        diff = case['scores'][j]['total'] - sum(case['scores'][j]['scores'])
        if diff == 0:
            if s >= case['min_score']:
                # These scores are above min_score
                case['above_min_score'] += 1
            else:
                if case['surprise_rem'] > 0 and s > 0 and s + 1 >= case['min_score']:
                    # Actually adjust the scores for testing
                    case['scores'][j]['scores'][0] += 1
                    case['scores'][j]['scores'][2] -= 1

                    case['above_min_score'] +=1
                    case['surprise_rem'] -= 1
        elif diff == 1:
            if s >= case['min_score'] or s + 1 >= case['min_score']:
                # Actually adjust the scores for testing
                case['scores'][j]['scores'][0] += 1

                case['above_min_score'] += 1
            else:
                if case['surprise_rem'] > 0 and s + 1 >= case['min_score']:
                    # Actually adjust the scores for testing
                    case['scores'][j]['scores'][0] += 1
                    case['scores'][j]['scores'][2] -= 1

                    case['above_min_score'] += 1
                    case['surprise_rem'] -= 1
        elif diff == 2:
            if s >= case['min_score'] or s + 1 >= case['min_score']:
                # Actually adjust the scores for testing
                case['scores'][j]['scores'][0] += 1
                case['scores'][j]['scores'][1] += 1

                case['above_min_score'] += 1
            else:
                if case['surprise_rem'] > 0 and s + 2 >= case['min_score']:
                    # Actually adjust the scores for testing
                    case['scores'][j]['scores'][0] += 1
                    case['scores'][j]['scores'][2] -= 1

                    case['above_min_score'] += 1
                    case['surprise_rem'] -= 1
        else:
            raise Exception('Score difference > 2 %s' % (str(case['scores']),))

        cases[i] = case
    print case

# Output
with open(file + '.out', 'w') as output:
    for i, case in enumerate(cases):
        output.write("Case #%d: %d\n" % (i+1, case['above_min_score']))
