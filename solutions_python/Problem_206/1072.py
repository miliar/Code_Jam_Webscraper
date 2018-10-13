import fileinput

def solve(s, v, d):
    # aren't linear kinematics great!
    return (v * d) / (d -s)


for c in range(1, int(input().strip()) + 1):
    d, n = map(int, input().strip().split())
    horses = [list(map(int, input().strip().split())) for i in range(n)]
    ans = 100000000000000
    for horse in horses:
        max_spd = solve(horse[0], horse[1], d) 
        if max_spd < ans:
            ans = max_spd
    print("Case #{}: {}".format(c, ans))
    
