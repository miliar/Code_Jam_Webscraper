d = {}

def winning(A, B):
    if A <= 0 or B <= 0:
        return True
    if (A, B) in d:
        return d[(A, B)]
    if A < B:
        A, B = B, A
    win = False
    for C in range(A % B, A, B):
        if winning(C, B):
            continue
        else:
            d[(A, B)] = True
            return True
    d[(A, B)] = False
    return False

def solve(A1, A2, B1, B2):
    c = 0
    for A in range(A1, A2 + 1):
        for B in range(B1, B2 + 1):
            if winning(A, B):
                c += 1
    return c
    
def main():
    T = int(input())
    for i in range(T):
        A1, A2, B1, B2 = map(int, input().split())
        print("Case #{}:".format(i + 1), solve(A1, A2, B1, B2))

if __name__ == "__main__":
    main()

