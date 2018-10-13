#global variable
next = 0
tagged = 0

#returns (ln,cn) of the lesser neighbour of (l,c). (l, c) is returned if elt is sink
def Less(l, c, map):
    #checks element out of boundries
    if c < 0 or c > len(map[0]) or l < 0 or l > len(map):
        return "OutOfBoundries"
    
    else:
        less = (l, c, map[l][c][0])
        #checks North
        if l >= 1 and map[l-1][c][0] < less[2]: less = (l-1, c, map[l-1][c][0])
        #checks West
        if c >= 1 and map[l][c-1][0] < less[2]: less = (l, c-1, map[l][c-1][0])
        #checks East
        if c < len(map[0])-1 and map[l][c+1][0] < less[2]: less = (l, c+1, map[l][c+1][0])
        #checks South
        if l < len(map)-1 and map[l+1][c][0] < less[2]: less = (l+1, c, map[l+1][c][0])
    return (less[0], less[1])

#finds the basin for
def Basin(l, c, map):
    global next
    global tagged
    
    less = Less(l, c, map)
    
    #checks element out of boundries
    if less == "OutOfBoundries":
        return "OutOfBoundries"
    
    #Base
    else:
        #Base 1: (l,c) is Sink
        if less == (l, c) and map[l][c][1] == '@': 
            map[l][c][1] = chr(ord('a') + next)
            next += 1
            tagged += 1
            #print map[l][c][1], next
            return map[l][c][1]
        elif map[l][c][1] != '@':
            return map[l][c][1]
        #Hip + Step: Recurs in small
        elif less != (l, c):
            map[l][c][1] = Basin(less[0], less[1], map)
            tagged += 1
            return map[l][c][1]
    
    
def main():
    global tagged
    global next
    t = int(raw_input())
    
    #t maps follow
    for i in range(1,t+1):
        h, w = raw_input().split()
        h = int(h)
        w = int(w)
        tagged = 0
        next = 0
        
        #reads each line from N to S
        aux = []
        map = []
        for j in range(h):
            aux.append(raw_input().split())
        for j in aux:
            line = []
            for k in j:
                line.append([int(k), '@']) # @ represents a non-labled region
            map.append(line)
        
        #continues while there are untagged elts
        l = 0
        c = 0
        while tagged < h*w:
            Basin(l,c,map)
            c += 1
            if c == w:
                c = 0
                l += 1
            
        print "Case #" + str(i) + ":" 
        for k in range(h):
            for j in range(w):
                print map[k][j][1],
            print ""
        
        
if __name__ == "__main__":
    main()