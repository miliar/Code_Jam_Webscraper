import sys

r = sys.stdin.readline

T = int(r())

for i in range(T):
    C,F,X = map(float, r().split())
    time_count = 0.0
    production = 2
    while True:
        # Make a decision
        no_new_farm_t = X/(production)
        with_new_farm_t = C/production + X / (production + F)
        if no_new_farm_t <= with_new_farm_t:
            time_count += no_new_farm_t
            print("Case #%d: %.8f" % (i+1,time_count))
            break
        else:
            time_count += C/production
            production += F
