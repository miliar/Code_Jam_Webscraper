def main(D, l):
    t = max((D-k)/s for k,s in l)
    return D/t


for case in range(int(input())):
    D, n = map(int, input().split())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    ans = main(D, l)
    print('Case #%i: %.06f' % (case + 1, ans))