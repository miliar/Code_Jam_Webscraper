if __name__ == "__main__":
    T = int(raw_input())
    for _ in range(T):
        r, c, w = map(int, raw_input().split())
        if c % w == 0:
            score = r * (c / w) + w - 1
        else:
            score = r * (c / w) + w
        print 'Case #{}: {}'.format(_ + 1, score)
