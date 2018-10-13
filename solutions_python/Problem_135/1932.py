def main():
    blah = []
    with open('A-small-attempt0.in', 'r') as f:
        T = int(f.readline())    
        for test_case in xrange(T):
            first_answer = int(f.readline())
            card_matrix1 = [[int(x) for x in f.readline().split()] for row in xrange(4)]
            second_answer = int(f.readline())
            card_matrix2= [[int(x) for x in f.readline().split()] for row in xrange(4)]

            first_row_of_interest = card_matrix1[first_answer - 1]
            second_row_of_interest = card_matrix2[second_answer - 1]
            
            intersection = list(set(first_row_of_interest) & set(second_row_of_interest))
            if len(intersection) == 1:
                answer = str(intersection[0])
            elif len(intersection) > 1:
                answer = "Bad magician!"
            else:
                answer = "Volunteer cheated!"
            blah.append("Case #" + str(test_case + 1) + ": " + answer + '\n')

    with open('output.txt','w') as o:
        for thing in blah:
            o.write(thing)
    

if __name__ == '__main__':
    main()
