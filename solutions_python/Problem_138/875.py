from collections import deque

def solve(N, enemyWeights, ownWeights):
    allWeights = sorted(enemyWeights + ownWeights)
    rankMap = {weight: rank for (rank, weight) in enumerate(allWeights)}
    enemyWeights = sorted([rankMap[weight] for weight in enemyWeights])
    ownWeights = sorted([rankMap[weight] for weight in ownWeights])
    print ownWeights
    print enemyWeights
    # solve war
    enemy = deque(enemyWeights)
    own = deque(ownWeights)
    while enemy and own:
        while enemy[0] < own[0]:
            enemy.popleft()
            if not enemy or not own:
                break
        if not own or not enemy:
            break
        own.popleft()
        enemy.popleft()
    z = len(own)   
    
    # solve deceitful war
    enemy = deque(enemyWeights)
    own = deque(ownWeights)
    y = 0
    while own:
        if own[0] > enemy[0]:
            y += 1
            own.popleft()
            enemy.popleft()
        else:
            own.popleft()
            enemy.pop()
        #print own
        #print enemy
    return "{} {}".format(y, z)
    
def main():
    fin = open("D-large.in")
    fout = open("a.txt", 'w')
    T = int(fin.readline())
    for i in range(T):
        N = int(fin.readline())
        ownWeights = map(float, fin.readline().split(' '))
        enemyWeights = map(float, fin.readline().split(' '))
        ans = solve(N, enemyWeights, ownWeights)
        fout.write("Case #{}: {}\n".format(i+1, ans))

if __name__ == '__main__':
    main()
        
