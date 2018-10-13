
input_path = 'C:/A-small-attempt0.in'


def read_file(path):
    with open(path, mode='r', encoding='utf8') as file:
        test_cases = file.readline()
        # first arrangement
       

        for j in range(0, int(test_cases)):
            
            first_answer = file.readline()
            for i in range(0, 4):
                if i == int(first_answer) -1:
                    first_card_array = set( [int(x) for x in file.readline().split()] )
                else:
                    file.readline()
            #print(first_card_array)
            
            # second arrangement
            second_answer = file.readline()

            for i in range(0, 4):
                if i == int(second_answer)-1:
                    second_card_array = set ([ int(x) for x in file.readline().split()])
                else:
                    file.readline()
                    
            #print(second_card_array)

            answer = first_card_array & second_card_array
            if len(answer) == 1:
                msg = str(answer.pop())
            elif len(answer) > 1:
                msg = 'Bad magician!'
            else:
                msg = 'Volunteer cheated!'
            
            print('Case #%s: %s' %(j+1, msg))
        file.close()


read_file(input_path)
