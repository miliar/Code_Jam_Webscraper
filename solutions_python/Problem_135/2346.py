from __future__ import print_function

T = int(input())
for i in range(T):
    p = int(input())
    A = [map(int, input().split(' ')) for j in range(4)]
    q = int(input())
    B = [map(int, input().split(' ')) for j in range(4)]

    cards = list(set(A[p-1]) & set(B[q-1]))

    if len(cards) == 1:
        print("Case #{n}: {c}".format(n=i+1, c=cards[0]))
    elif len(cards) == 0:
        print("Case #{n}: Volunteer cheated!".format(n=i+1))
    else:
        print("Case #{n}: Bad magician!".format(n=i+1))
