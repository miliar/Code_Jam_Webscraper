for t in range(int(input())):

    _, s = str.split(input())
    friends = standing = 0
    for level, count in enumerate(map(int, s)):

        friends += max(0, level - standing - friends)
        standing += count

    print(str.format("Case #{}: {}", t + 1, friends))
