import sys
import itertools



def main():
    file = sys.stdin
    lines = iter(file.readlines())

    testCase = int(lines.next())
    caseNo = itertools.count(1)

    while testCase:
        answer_first = int(lines.next())
        numbers_list_first = list()
        for i in range(4):
            row = map(int, lines.next().lstrip().rstrip().split(' '))
            numbers_list_first.append(row)
        possible_answer_first = numbers_list_first[answer_first-1]
        
        answer_second = int(lines.next())
        numbers_list_second = list()
        for i in range(4):
            row = map(int, lines.next().lstrip().rstrip().split(' '))
            numbers_list_second.append(row)
        possible_answer_second = numbers_list_second[answer_second-1]

        
        ###########checking if bad magician/ cheater

        number_of_conflict = 0
        for p in possible_answer_first:
            if p in possible_answer_second:
                number_of_conflict += 1
                conflict_number = p
           
        if number_of_conflict == 1:
            print 'Case #%d: %s'%(caseNo.next(), conflict_number)
        elif number_of_conflict==0:
            print 'Case #%d: %s'%(caseNo.next(), 'Volunteer cheated!')
        else:
            print 'Case #%d: %s'%(caseNo.next(), 'Bad magician!')
        #print 'conflicts ', number_of_non_conflict, conflict_number
        testCase -= 1        

if __name__ == '__main__':
    main()
