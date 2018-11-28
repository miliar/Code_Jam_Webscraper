# Google code jam 2016
# Qualification Round - ..

import time

file_name = 'A-large';
input_file = open(file_name + '.in', 'r')
output_file = open(file_name  + '.out', 'w')

def main_function(caseNumber, D, N, horses):

    maxHours = 0
    for horse in horses:
        hours = (D - horse['K']) / horse['S']
        if hours > maxHours:
            maxHours = hours


    print_result(caseNumber, D / maxHours)


def print_result(caseNumber, output1):
    printnumber = format(output1, '7.6f')
    print("Case #{}: {}".format(caseNumber, printnumber))

    output_file.write("Case #{}: {}\n".format(caseNumber, output1))

def read_input_file():
    numberOfCases = int(input_file.readline())

    for caseNumber in range(1, numberOfCases + 1):
        # read input
        D, N = input_file.readline().rstrip().split(' ')
        horses = []

        for idx in range(0, int(N)):
            K, S = input_file.readline().rstrip().split(' ')
            horses.append({'K': int(K), 'S': int(S)})

        main_function(caseNumber, int(D), int(N), horses)

print('Starting ...')

start_time = time.time()

read_input_file()
input_file.close()
output_file.close()

end_time = round((start_time - time.time()) / 1000, 2)

print('Done! (Finished in {}ms)'.format(end_time))
