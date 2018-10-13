diff = lambda a, b: abs(a - b)

def solve(n, arr):
    last = arr[0]
    total = local = 0
    location = dict(O=1, B=1)
    for i in range(n):
        actor, place = arr[2*i : 2*i + 2]
        place = int(place)
        if actor == last:
            local += diff(place, location[actor]) + 1
        else:
            dist = diff(place, location[actor])
            total += local
            if dist <= local:
                local = 1
            else:
                local = (dist - local) + 1
        #print actor, place, location[actor], local
        location[actor] = place
        last = actor
    return total + local

with open ('A-large.in') as f:
    t = int(f.readline())
    for i in range(t):
        arr = f.readline().split(' ')
        n = int(arr[0])
        print 'Case #{0}: {1}'.format(i+1 ,solve(n, arr[1:]))
