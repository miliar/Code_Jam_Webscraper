import io

def read_input(filepath):
    with open(filepath, 'r') as f:
        content = f.read().splitlines()
    return content

def write_output(filepath, answers):
    with open(filepath, 'w') as f:
        for i in range(len(answers)):
            print 'Case #' + str(i+1) + ': ' + str(answers[i])
            f.write('Case #' + str(i+1) + ': ' + str(answers[i]) + '\n')

'''for each test case'''
def run_each(case):
    s_max = int(case[0])
    answer = 0
    lists = [int(c) for c in case[2:]]
    if len(lists) == 1:
        return 0
    else:
        total_people = lists[0]
        for idx in range(1, s_max+1):
            if total_people < idx:
                answer += (idx-total_people)
                total_people += (idx-total_people) + lists[idx]
            else:
                total_people += lists[idx]
        return answer

'''for all test cases'''
def run(cases):
    answer = []
    for c in cases:
        answer.append(run_each(c))
    return answer

if __name__ == '__main__':
    content = read_input('/Users/yiyang/Desktop/codejam/1/A-small-attempt0.in')
    T = int(content[0])
    cases = content[1:]
    print cases
    
    answer = run(cases)
    write_output('/Users/yiyang/Desktop/codejam/1/input.output', answer)