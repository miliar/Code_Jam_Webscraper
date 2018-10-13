error_msg = "IMPOSSIBLE"

def one_flipper(pancakes, previous):
    for i in range(0,min(len(pancakes),len(previous))):
        pancakes[i] *= previous[i]

    m = 1
    flips = []
    k = len(pancakes)
    for i in range(0,k) :
        if pancakes[i] == m :
            flips.append(i)
            m *= -1

    flip_number = len(flips)
    previous = []
    last_flip = -1

    if flip_number > 0 :
        if flips[0] != 0:
            flips.insert(0, 0)
        
        if len(flips) > 1:
            last_flip = flips[-1]
            previous = [1] * flips[-1]
            m = -1
            for i in range(len(flips),1,-1):
                x, y = flips[i-2:i]
                previous[x:y] = [m] * (y - x)
                m *= -1
        
                

    return flip_number, previous, last_flip


def flip_cakes(cakes, flip_size):
    
    i = 0
    length = len(cakes)
    number = 0
    previous = []

    while i < length :
                
        flip_number, previous , last_flip = one_flipper(cakes[i:min(length,i+flip_size)],previous)
        
        i += flip_size

        if last_flip > 0 and (i + last_flip) > length:
            break
        
        number += flip_number
        
        if (i == length and flip_number == 1):
            return number
        
        if (i > length and flip_number == 0):
            return number
        
        
    return error_msg

    
def flip_pancakes(pancakes, flip_size):

    length = len(pancakes)
    i = 0
    while i < length and pancakes[i] < 0:
        i += 1
        
    if i >= length:
        return 0
    
    j = length
    while pancakes[j-1] < 0:
        j -= 1
        
    if (j - i) < flip_size:
        return error_msg
    
    if i >= (length - j):
        cakes = pancakes[i:j]
    else:
        cakes = pancakes[(j-1)::-1]

    return flip_cakes(cakes, flip_size)


t = int(input())
for i in range(1, t + 1):
    cakes, k = input().split(" ")

    pancakes = [ord(x)-44 for x in cakes]
    n = flip_pancakes(pancakes,int(k))
    
    print("Case #{}: {}".format(i, n))
