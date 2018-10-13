for t in range(input()):
    print "Case #%s:" % str(t + 1),
    C, F, X = map(float, raw_input().split())
    time = 0.0
    I = 2
    while X / I > C / I + X / (I + F):
        time += C / I
        I += F
    time += X / I
    print time