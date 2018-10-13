import copy

def main():
  T = int(raw_input())
  for i in range(T):
      D, N = raw_input().split(' ')
      D, N = int(D), int(N)
      H = []
      for j in range(N):
          K, S = raw_input().split(' ')
          K, S = int(K), int(S)
          H.append((K, S))
      result = run_case(D, N, H)
      print 'Case #{}: {:.6f}'.format(i+1, result)


def run_case(D, N, H):
    # sort horses
    H = sorted(H, key=lambda x: x[0])

    # update velocities
    K = [x[0] for x in H]
    S = [x[1] for x in H]
    for i in range(N-1, 0, -1):
        if S[i] >= S[i-1]: continue
        I = float( S[i-1] * (K[i] - K[i-1]) ) / (S[i-1] - S[i])
        I = I + K[i-1]
        if I > D: continue
        T0 = float(I - K[i-1]) / S[i-1]
        T1 = float(D - I) / S[i]
        T = T0 + T1
        avg_velocity = float(D - K[i-1]) / T
        S[i-1] = avg_velocity

    # find last horse time to D
    total_time = float(D - K[0]) / S[0]
    return D / total_time


if __name__ == '__main__':
    main()
