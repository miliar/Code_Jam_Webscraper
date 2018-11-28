
def A():
    input_file = open("input", "r")
    output_file = open("output", "w")

    examples = int(input_file.readline())
    for example in range(examples):

        common = '0'
        
        first_index = int(input_file.readline())
        for ignore in range(first_index-1):
            input_file.readline()
        first_row = input_file.readline()
        first_row = [int(i) for i in first_row.split()]
        for ignore in range(4-first_index):
            input_file.readline()

        second_index = int(input_file.readline())
        for ignore in range(second_index-1):
            input_file.readline()
        second_row = input_file.readline()
        second_row = [int(i) for i in second_row.split()]
        for ignore in range(4-second_index):
            input_file.readline()

        for i in first_row:
            if i in second_row:
                if common == '0':
                    common = str(i)
                else:
                    common = 'Bad magician!'

        if common == '0':
            output_file.write("".join(['Case #', str(example+1), ': Volunteer cheated!\n']))
        else:
            output_file.write("".join(['Case #', str(example+1), ': ', common, '\n']))
            
    input_file.close()
    output_file.close()



def B():
    input_file = open("input", "r")
    output_file = open("output", "w")

    examples = int(input_file.readline())
    for example in range(examples):
        
        C, F, X = [float(i) for i in input_file.readline().split()]
        time = 0.0
        rate = 2.0
        
        while True:
            if X/rate <= X/(rate+F) + C/rate:
                output_file.write("".join(['Case #', str(example+1), ': ', str(round(time+X/rate,7)), '\n']))
                break
            else:
                time = time + C/rate
                rate = rate + F

    input_file.close()
    output_file.close()

























