

T = int(input())

for lt in range(1, T+1):
    r, c = map(int, input().split())
    mp = [list(input()) for _ in range(r)]
    
    for line in mp:
        
        ind = 0
        draw_ch = "" 
        for i, ch in enumerate(line):
            if ch != '?':
                draw_ch = ch
                for j in range(ind, i):
                    line[j] = ch
                ind = i+1
        
        if draw_ch:
            for j in range(ind, c):
                line[j] = draw_ch
        
    
    ind = 0
    draw_line = []
    for i, line in enumerate(mp):
        if "".join(line) != "?"*c:
            draw_line = line
            for j in range(ind, i):
                mp[j] = draw_line[0:c]
            ind = i+1

    for j in range(ind, r):
        mp[j] = draw_line[0:c]

    print("Case #%d:" % lt)

    for line in mp:
        print("".join(line))
