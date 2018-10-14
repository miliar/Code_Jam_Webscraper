# Google code jam 2016
# Qualification Round - ..

import time

file_name = 'C-small';
input_file = open(file_name + '.in', 'r')
output_file = open(file_name  + '.out', 'w')

def main_function(caseNumber, bathrooms, people):
    bathroomUsage = [bathrooms]

    for index in range(0, people):
        preferredLocation = bathroomUsage.index(max(bathroomUsage))
        maxSpace = int(bathroomUsage[preferredLocation] / 2)

        if bathroomUsage[preferredLocation] % 2 == 0:
            bathroomUsage[preferredLocation] = int(bathroomUsage[preferredLocation] / 2 - 1)
            bathroomUsage.insert(preferredLocation + 1, bathroomUsage[preferredLocation] + 1)
        else:
            bathroomUsage[preferredLocation] = int(bathroomUsage[preferredLocation] / 2)
            bathroomUsage.insert(preferredLocation + 1, bathroomUsage[preferredLocation])

    print_result(caseNumber, maxSpace, min(bathroomUsage))


def print_result(caseNumber, maxSpace, minSpace):
    print("Case #{}: {} {}".format(caseNumber, maxSpace, minSpace))

    output_file.write("Case #{}: {} {}\n".format(caseNumber, maxSpace, minSpace))

def read_input_file():
    numberOfCases = int(input_file.readline())

    for caseNumber in range(1, numberOfCases + 1):
        # read input
        bathrooms, people = input_file.readline().rstrip().split(' ')
        main_function(caseNumber, int(bathrooms), int(people))

print('Starting ...')

start_time = time.time()

read_input_file()
input_file.close()
output_file.close()

end_time = round((start_time - time.time()) / 1000, 2)

print('Done! (Finished in {}ms)'.format(end_time))
