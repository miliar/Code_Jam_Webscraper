
def process_game():
    C, F, X = map(float, raw_input().split())
    r = 2.0
    best_time = X / r
    time_to_farm = C / r
    r += F
    time_with_farm = time_to_farm + X / r
    while (time_with_farm < best_time):
        best_time = time_with_farm
        time_to_farm += C / r
        r += F
        time_with_farm = time_to_farm + X / r
    print best_time

for i in xrange(1, int(raw_input()) + 1):
    print "Case #%d:" % (i),
    process_game()
