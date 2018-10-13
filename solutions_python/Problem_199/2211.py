T = int(input())
for i in range(0, T):

    flips = 0

    # Get input
    pancakes = input().split()
    S = list(pancakes[0])
    K = int(pancakes[1])

    # Find next -
    for j in range(0, len(S) - K + 1):
        if S[j] == '-':
            # Flip
            flips += 1
            for p in range(j, j+K):
                if S[p] == '-':
                    S[p] = '+'
                else:
                    S[p] = '-'
    # print(S)

    # Check if has - left
    for j in range(len(S)-K+1, len(S)):
        # print("Index " + str(j))
        if S[j] == '-':
            flips = -1

    # Final result
    if (flips >= 0):
        print("Case #" + str(i+1) + ": " + str(flips))
    else:
        print("Case #" + str(i+1) + ": IMPOSSIBLE")
