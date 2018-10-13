def max_speed(D, N, KSpairs):
    
    KSpairs.sort(reverse=True)
    
    KILOMETER = 0
    SPEED = 1
    
    Ts = [None]*N
    Ts[0] = (D - KSpairs[0][KILOMETER]) / float(KSpairs[0][SPEED])
    
    for i in range(1,N):
        candidate = (D - KSpairs[i][KILOMETER]) / float(KSpairs[i][SPEED])
        Ts[i] = max(Ts[i-1], candidate)
    
    return D/float(Ts[N-1])