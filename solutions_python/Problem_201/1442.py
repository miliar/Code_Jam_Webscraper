

def move_people(N,K):
    import math
    free_range = []
    new_range = [N]
    result = ''
    while(K > 0):
        free_range = new_range
        new_range = []
        free_range = sorted(free_range,reverse=True)
        
        for rang in free_range:
            result = [math.floor((rang - 1) / 2), math.ceil((rang - 1) / 2)]
            if(result == [0,0]):
                break
            new_range += result
            K -= 1
            if (K == 0):
                break
        if(result == [0,0]):
            break
    return result

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    try:
        file = open(file,'r')
    except IOError:
        print("Can't open file")

    T = int(file.readline().rstrip())
    for i in range(T):
        N, K = file.readline().rstrip().split(" ")
        result = move_people(int(N),int(K))
        print("Case #{0}: {1} {2}".format(i+1,max(result), min(result)) )
