#
# Code Jam Problem A
#

def find(array):
    current_aud = array[0]
    friends = 0
    index = 1
    for ele in array[1:]:
        if ele == 0:
            index += 1
            continue
        if current_aud < index:
            friends += (index - current_aud)
            current_aud += (index - current_aud + ele)
            index += 1
        else:
            index += 1
            current_aud += ele
    return friends

data = []
for line in open('A-large.in'):
    data.append(line.split(' '))

array = []
f = open('A-large.out', 'w')

index = 1
for line in data[1:]:
    array = [int(i) for i in line[1].split('\n')[0]]
    f.write('Case #%s:'%(index)+' '+str(find(array))+'\n')
    index += 1
    find(array)

f.close()
