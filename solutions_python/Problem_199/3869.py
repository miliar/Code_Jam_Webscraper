#Pancake Sorting Variance
#Author Maxie
#ver 1.0

filename= 'Ainput.txt'
file= open(filename, 'r')
data= file.readlines()
file.close()
case = 0
output= open('Aoutput.txt', 'w')


del(data[0])


for index in range(len(data)):
    list= data[index].replace('\n', '')


def flip(pancakes, case, length):
    flipping = 0
    while sum(pancakes) != length:
        for index in range(length):
            if length - index < N and sum(pancakes) != length:
                output.write('Case #' +str(case)+': IMPOSSIBLE\n')
                return
            if pancakes[index] == 0:
                flipping += 1
                for flipped in range(index, index + N):
                    if pancakes[flipped] == 0:
                        pancakes[flipped] = 1
                    else:
                        pancakes[flipped] = 0
    output.write('Case #' +str(case)+': '+str(flipping)+'\n')

for items in data:
    case+= 1
    pancakes= []
    for indexin in range(len(items)-2):
        if items[indexin]== '+':
            pancakes.append(1)
        elif items[indexin]== '-':
            pancakes.append(0)
    N= items.split()
    N= int(N[1])
    length = len(pancakes)
    flip(pancakes, case,length)

output.close()



