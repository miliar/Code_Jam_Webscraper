def flip(S, K, i):
    head = S[:i]
    tail = S[i+K:]
    mid  = ''.join(['-' if S[i+j]=='+' else '+' for j in range(K)])
    return head + mid + tail

def solve(S, K):
    count = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            S = flip(S, K, i)
            count += 1
    for i in range(len(S)-K+1, len(S)):
        if S[i] == '-':
            return 'IMPOSSIBLE'
    return count


def main():
    T = input()

    for i in range(T):
        S, K = raw_input().split()
        K = int(K)
        print 'Case #{}:'.format(i+1), solve(S,K)

if __name__ == '__main__':
     main()
