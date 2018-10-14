def calcAmount(A, B, K):
    count = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                count += 1
    return count

def main():
    out = "Case #{}: {}"
    cases = int(input())
    for case in range(1, cases + 1):
        A, B, K = [int(num) for num in input().split()]
        amount = calcAmount(A, B, K)
        print(out.format(case, amount))

main()