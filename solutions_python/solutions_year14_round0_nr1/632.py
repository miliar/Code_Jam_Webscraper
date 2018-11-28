from parser import parse

def helper(test):
    row1 = test[0]
    row2 = test[5]
    possible1 = test[row1]
    possible2 = test[row2+5]
    answers = []
    for i in possible1:
        if i in possible2:
            answers.append(i)
    if not answers:
        return "Volunteer cheated!"
    elif len(answers) > 1:
        return "Bad magician!"
    return answers[0]

# schema here
f = lambda l: [int(x) for x in l.split()]
schema = [(),[int, f, f, f, f, int, f, f, f, f]]

num_tests,tests = parse(schema)
for case,test in enumerate(tests):
	sol = helper(test)
	print 'Case #{}: {}'.format(case+1, sol)
