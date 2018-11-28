T = int(raw_input())
#
f = open('output3_3.txt', 'w')

def final_comp(N):
    if N % 2 == 0:
        return N / 2,(N / 2) - 1
    else:
        return (N - 1) / 2, (N - 1) / 2


def division(N,K):
    if K == 1:
        return final_comp(N)
    else:
        i = 1
        sumi = 0
        orig_N = N
        while sumi < K:
            if N%2 == 0:
                N = N/2
            else:
                N = (N-1)/2
            sumi += i
            i = i*2
            # print N,sumi
            if sumi + i >= K:
                i = i/2
                break
        q = N * i* 2 - (orig_N - sumi)
        p = i * 2 - q
        if K - sumi - p > 0:
            N -= 1
        return final_comp(N)

for _ in range(1,T+1):
    N,K = map(int,raw_input().split())
    ans_H,ans_L = division(N,K)
    print ans_H,ans_L
    f.write("Case #" + str(_) + ": " + str(ans_H) + " "+str(ans_L)+"\n")

f.close()