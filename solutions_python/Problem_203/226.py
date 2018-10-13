
t = int(input())  # read a line with a single integer
for k in range(1, t + 1):
    r, c = [int(s) for s in input().split(" ")]
    seen = set()
    chars = []

    for i in range(r):
        chars.append(list(input()))

    for r_ in range(r):
        for c_ in range(c):
            top = r_ - 1
            bottom = r_ + 1
            left = c_ - 1
            right = c_ + 1

            if chars[r_][c_] == '?':
                continue

            me = chars[r_][c_]
            if me in seen:
                continue
            seen.add(me)

            while left >= 0 and chars[r_][left] == "?":
                chars[r_][left] = me
                left -= 1
            left += 1

            while right < c and chars[r_][right] == "?":
                chars[r_][right] = me
                right += 1
            right -= 1

            while top >= 0 and sum([chars[top][b] == "?" for b in range(left, right + 1)]) == (right + 1- left) :
                for f in range(left, right + 1):
                    chars[top][f] = me
                top -= 1

            while bottom < r and sum([chars[bottom][d] == "?" for d in range(left, right + 1)]) == (right + 1 - left) :
                for e in range(left, right + 1):
                    chars[bottom][e] = me
                bottom += 1

    print("Case #{}:".format(k))
    for a in chars:
        print("".join(a))
