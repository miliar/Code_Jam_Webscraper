import sys

file_in = open(sys.argv[1])

n = int(file_in.readline())

result = []

for i in xrange(n):
    rides, limit, _ = map( int, file_in.readline().rstrip('\n').split() )
    groups = map( int, file_in.readline().rstrip('\n').split() )
    
    money = 0
    
    for _ in xrange(rides):
        people = 0
        running = []
        while True:
            if not groups:
                money += people
                break
            g = groups.pop(0)
            people += g
            if people > limit:
                groups.insert(0, g)
                people -= g
                money += people
                break
            else:
                running.append(g)
        groups.extend(running)
        
    
    result.append( 'Case #%s: %s' % (i+1, money) )


file_in.close()

with open('output.txt', 'w') as out:
    out.write('\n'.join(result))
