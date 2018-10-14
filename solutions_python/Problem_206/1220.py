import sys
sys.stdout = open("./output.txt", "w")

t = input()
for i in range(t):
    dest, horses = [int(s) for s in raw_input().split(" ")]
    maxtime = 0
    for h in range(horses):
        pos, speed = [int(s) for s in raw_input().split(" ")]
        time = float(dest - pos) / speed
        if maxtime < time:
            maxtime = time
    ans = float(dest) / maxtime
    print("Case #%d: %.6f"%( i+1, ans ))
