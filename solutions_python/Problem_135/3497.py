def FindSimmilars(row1, row2):
    row1 = row1.split(' ')
    row2 = row2.split(' ')
    counter = 0
    answer = ''
    for i in row1:
        for j in row2:
            if i == j:
                counter = counter + 1
                answer = j
    if counter == 0:
        return 'Volunteer cheated!'
    elif counter == 1:
        return answer
    else:
        return 'Bad magician!'
    
def main():
    f = open('A-small-attempt2.in', 'r')
    o = open('A-small-attempt2.out','w')
    limit = f.readline()
    
    for i in range(int(limit)):
        answer1 = f.readline()
        field1 = []
        for j in range(4):
            field1 = field1 + [f.readline()]
        answer2 = f.readline()
        field2 = []
        for j in range(4):
            field2 = field2 + [f.readline()]
        answer = FindSimmilars(field1[int(answer1)-1][:-1], field2[int(answer2)-1][:-1])
        o.write('Case #' + str(i + 1) + ': ' + answer + '\n')
    o.close()
    f.close()