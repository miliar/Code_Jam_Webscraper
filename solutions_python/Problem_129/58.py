import sys

def getPath(people):
    st = ed = 0
    p = 0x7FFFFFFF
    np = 0
    j = 0
    while(people[j] == 0):
        st = j + 1
        j += 1
        if j >= len(people):
            return True, None, None, None
    for j in range(st, len(people)):
        np += people[j]
        if(np <= 0):
            ed = j
            return False, st, ed, p
        p = min(p, np)

def calFee(st, ed, N):
    return - (1 / 2) * (ed - st) * (-1 + ed - 2 * N - st)

if __name__=='__main__':
    n = int(sys.stdin.readline())
    for i in range(n):
        sys.stdout.write("Case #{}: ".format(i + 1))
        stations, pair = tuple(map(int, sys.stdin.readline().split()))
        travellers = []
        people = [0 for j in range(stations + 1)]
        savedFee = 0
        for j in range(pair):
            traveller = tuple(map(int, sys.stdin.readline().split()))
            savedFee += calFee(traveller[0], traveller[1], stations) * traveller[2]
            people[traveller[0]] += traveller[2]
            people[traveller[1]] -= traveller[2]
            travellers.append(traveller)
        while(True):
            finish, st, ed, p = getPath(people)
            if(finish):
                break
            savedFee -= calFee(st, ed, stations) * p
            people[st] -= p
            people[ed] += p
        sys.stdout.write("{}\n".format(int(savedFee % 1000002013)))

