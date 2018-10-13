__author__ = 'vaibhav'

f = open('A-small-attempt3.in')
f1 = open('output.txt', 'w')

no_of_cases = int(f.readline())
for i in range(0, no_of_cases):
    first = int(f.readline())
    first_set = ''
    second_set = ''
    if first == 1:
        first_set = f.readline()
        f.readline()
        f.readline()
        f.readline()
    if first == 2:
        f.readline()
        first_set = f.readline()
        f.readline()
        f.readline()
    if first == 3:
        f.readline()
        f.readline()
        first_set = f.readline()
        f.readline()
    if first == 4:
        f.readline()
        f.readline()
        f.readline()
        first_set = f.readline()

    second = int(f.readline())
    if second == 1:
        second_set = f.readline()
        f.readline()
        f.readline()
        f.readline()
    if second == 2:
        f.readline()
        second_set = f.readline()
        f.readline()
        f.readline()
    if second == 3:
        f.readline()
        f.readline()
        second_set = f.readline()
        f.readline()
    if second == 4:
        f.readline()
        f.readline()
        f.readline()
        second_set = f.readline()

    first_set = first_set.replace('\n', '')
    second_set = second_set.replace('\n', '')
    row1 = set(map(int, first_set.split(' ')))
    row2 = set(map(int, second_set.split(' ')))
    answer = row1.intersection(row2)
    b = i+1
    if len(answer) == 1:
        f1.write("Case #" + str(b) + ": " + str(answer.pop()))
        f1.write('\n')
    elif len(answer) > 1:
        f1.write("Case #" + str(b) + ": " + 'Bad magician!')
        f1.write('\n')
    else:
        f1.write("Case #" + str(b) + ": " + 'Volunteer cheated!')
        f1.write('\n')
f.close()
f1.close()