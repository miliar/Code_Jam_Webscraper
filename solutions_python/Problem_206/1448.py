import numpy as np

def phase_input(houses):
    out_put = []
    for t in range(houses):
        out_put.append(input().split())
    
    return out_put
        
def main():
    test_times = int(input())
    for t in range(test_times):
        D, N = input().split()
        D = float(D)
        N = int(N)
        KS = np.array(phase_input(N), dtype = float)
        Annie_speed = D / max((D - KS.T[0]) / KS.T[1])
        print("Case #%d: %s" %(t + 1, Annie_speed))
    
if __name__ == '__main__':
    main()