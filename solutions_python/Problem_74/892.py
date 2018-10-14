def move(current, destination):
    if current < destination:
        return current + 1
    elif current > destination:
        return current - 1

f = open('A-large.in')
w = open('out.txt','w')

T = int(f.readline())
K = T
while T > 0:
    sequence = f.readline().split()
    t_presses = int(sequence[0])
    presses = 0
    sequence.remove(sequence[0])
    #sort into two sets
    blue_set = []
    orange_set = []
    i = 0
    while i < len(sequence):
        if sequence[i] == 'B':
            blue_set.append([str(sequence[i+1]),str(int(i/2+1))])
        elif sequence[i] == 'O':
            orange_set.append([str(sequence[i+1]),str(int(i/2+1))])
        i += 2
    blue = 1
    blue_presses = 0
    orange = 1
    orange_presses = 0
    seconds = 0
    a = 0
    while presses < t_presses:
        #blue move
        if blue_presses != len(blue_set):
            if blue != int(blue_set[blue_presses][0]):
                blue = move(blue, int(blue_set[blue_presses][0]))
            else:
                if int(blue_set[blue_presses][1]) - 1 == presses:
                    blue_presses += 1
                    a = 1
        #orange move
        if orange_presses != len(orange_set):
            if orange != int(orange_set[orange_presses][0]):
                orange = move(orange, int(orange_set[orange_presses][0]))
            else:
                if int(orange_set[orange_presses][1]) - 1 == presses:
                    orange_presses += 1
                    a = 1
        seconds += 1
        if a == 1:
            presses += 1
            a = 0
    

    w.write("Case #" + str(K-T+1) + ": " + str(seconds) +"\n")
    T -= 1

f.close()
w.close()
