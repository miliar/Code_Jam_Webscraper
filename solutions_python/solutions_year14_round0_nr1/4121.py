text_input = open('input.in')
test_cases = int(text_input.readline())
for test in range(test_cases):
    first_answer = int(text_input.readline())
    first_arrangement = []
    for i in range(4):
        line = text_input.readline()
        first_arrangement.append([int(i) for i in line.split(' ')])
    second_answer = int(text_input.readline())
    second_arrangement = []
    for i in range(4):
        line = text_input.readline()
        second_arrangement.append([int(i) for i in line.split(' ')])
    first_values = set(first_arrangement[first_answer-1])
    second_values = set(second_arrangement[second_answer-1])
    intersection = first_values & second_values
    if len(intersection) == 0:
        print 'Case #' + str(test+1) + ': Volunteer cheated!'
    elif len(intersection) == 1:
        print 'Case #' + str(test+1) + ': ' + str(intersection.pop())
    else:
        print 'Case #' + str(test+1) + ': Bad magician!'
text_input.close()
