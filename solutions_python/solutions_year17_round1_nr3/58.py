from collections import deque

for t in range(int(input())):
    print("Case #%s: " % str(t + 1), end="")
    (Hd, Ad, Hk, Ak, B, D) = map(int, input().split())
    q = deque([(0, Hd, Ad, Hk, Ak, "D")])
    while q:
        (c, hd, ad, hk, ak, f) = q.popleft()
        if hd <= 0 :
            continue
        if ad >= hk:
            print(c + 1)
            break
        if hd <= ak and hd < Hd and hd < Hd - ak:
            q.append((c + 1, Hd - ak, ad, hk, ak, f))  # C
        if f == "D" and ak > 0 and D > 0:
            q.append((c + 1, hd - ak + D, ad, hk, ak - D, f))  # D
            q.append((c + 1, hd - ak, ad + B, hk, ak, "B"))  # B
            q.append((c + 1, hd - ak, ad, hk - ad, ak, "A"))  # A
        elif f != "A" and B > 0:
            q.append((c + 1, hd - ak, ad + B, hk, ak, "B"))  # B
            q.append((c + 1, hd - ak, ad, hk - ad, ak, "A"))  # A
        q.append((c + 1, hd - ak, ad, hk - ad, ak, "A"))  # A
    else:
        print("IMPOSSIBLE")
