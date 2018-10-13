def get_number_of_sad_faces(configuration):
    count = configuration.count('-')
    return count


def swith_faces(configuration, start, end):
    new_configuration = configuration[0:start]
    for i in range(start, end):
        if configuration[i] == '+':
            new_configuration += '-'
        else:
            new_configuration += '+'
    new_configuration += configuration[end:]
    return new_configuration


def get_number_of_moves(configuration, k):
    sad_faces = get_number_of_sad_faces(configuration)
    if sad_faces == 0:
        return 0

    if len(configuration) == k and (sad_faces != 0 and sad_faces != k):
        return 'IMPOSSIBLE'

    configurations = {configuration}
    configuration_lenght = len(configuration)
    i = 0
    moves = 0
    while i < configuration_lenght:
        if configuration[i] == '-':
            if i + k > len(configuration):
                i = len(configuration) - k
            configuration = swith_faces(configuration, i, i + k)
            if configuration in configurations:
                return 'IMPOSSIBLE'
            configurations.add(configuration)
            moves += 1
        else:
            i += 1
    if get_number_of_sad_faces(configuration) == 0:
        return moves
    else:
        return 'IMPOSSIBLE'


t = int(input())
for i in range(1, t + 1):
    line = input().split(" ")
    configuration = line[0]
    k = int(line[1])
    print("Case #{}: {}".format(i, get_number_of_moves(configuration, k)))
