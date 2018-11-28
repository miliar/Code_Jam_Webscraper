def remove_edge(l):
    start = 0
    l = list(l)
    end = len(l)-1
    while(start <= end and l[start]):
        start+=1
    while(end >= start and l[end]):
        end-=1
    return l[start:end+1] if start<=end else []

def flip(l, pos, k):
    if pos+k > len(l):
        return False
    for i in range(pos,pos+k):
        l[i]+=1
    return True


def solution(l, k):
    to_2 = map(
        lambda x: 1 if x == '+' else 0,
        l
    )
    to_2 = remove_edge(to_2)
    if not to_2:
        return 0
    n = 0
    fliped = list(to_2)
    for i,c in enumerate(to_2):
        if fliped[i] % 2 != 1:
            n+=1
            if not flip(fliped, i, k):
                return 'IMPOSSIBLE'
    return n


K = int(input())
for i in range(K):
    l, k = input().split(' ')
    print('Case #{0}: {1}'.format(i+1, solution(l, int(k))))
