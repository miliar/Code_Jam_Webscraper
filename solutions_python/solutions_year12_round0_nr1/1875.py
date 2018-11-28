with open('speaking_in_tongues.txt') as f :
    lines = f.readlines()

number_of_cases = int(lines[0])

map =  {'a' : 'y', 'b' : 'h', 'c' : 'e', 'd' : 's', 'e' : 'o',
        'f' : 'c', 'g' : 'v', 'h' : 'x', 'i' : 'd', 'j' : 'u',
        'k' : 'i', 'l' : 'g', 'm' : 'l', 'n' : 'b', 'o' : 'k',
        'p' : 'r', 'q' : 'z', 'r' : 't', 's' : 'n', 't' : 'w',
        'u' : 'j', 'v' : 'p', 'w' : 'f', 'x' : 'm', 'y' : 'a',
        'z' : 'q'}

for i in range(number_of_cases) :
    case = lines[i + 1]
    case = case.replace('', '#')
    for key in map.keys() :
        case = case.replace(key + '#', map[key])
    with open('speaking_in_tongues_o.txt', 'a') as f :
        f.write('Case #' + str(i + 1) + ': ' + case.replace('#', ''))
