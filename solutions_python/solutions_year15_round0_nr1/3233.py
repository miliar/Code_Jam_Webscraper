
fn = 'in'
#fn = '/Users/vivanov/Downloads/B-large.in'
#fn = '/Users/vivanov/Downloads/B-small-attempt1.in'

with open(fn) as f:
    lines = f.read().splitlines()[1:]
    input_data = []
    i = 0
    while i < len(lines):
        if lines[i]:
            l = [k for k in lines[i].split(' ')]
            input_data.append({'audience': [int(j) for j in l[1]]})
            i += 1


def search(element):
        current_standing = 0
        audience = element['audience']
        num_friends_delta = 0
        num_friends = 0

        for i in range(len(audience)):
            shyness = i
            if not shyness <= current_standing and audience[i]:
                num_friends_delta += shyness - current_standing
            current_standing += audience[i] + num_friends_delta
            num_friends += num_friends_delta
            num_friends_delta = 0
        return num_friends



with open('out', 'w') as f :
    to_write = []
    for i in range(len(input_data)):
        element = input_data[i]
        res = search(element)
        print(i, res)
        to_write.append(('Case #%s: %s\n' %(i+1, res)))
    f.writelines(to_write)




