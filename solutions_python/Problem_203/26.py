def compute(cake):
    R, C = len(cake), len(cake[0])

    rows = [i for i in range(R) if set(cake[i]) != set(["?"])]
    
    # first fill the non-empty lines
    for i in rows: 
        cols = [j for j in range(C) if cake[i][j] != "?"] + [C]
        
        for j in range(cols[0]):
            cake[i][j] = cake[i][cols[0]]
        
        for k in range(len(cols)-1):
            for j in range(cols[k]+1, cols[k+1]):
                cake[i][j] = cake[i][cols[k]]

    # then fill the empty lines
    for i in range(rows[0]):
        cake[i] = cake[rows[0]][:]

    rows.append(R)
    for k in range(len(rows)-1):
        for j in range(rows[k]+1, rows[k+1]):
            cake[j] = cake[rows[k]][:]
            
    return cake
            
                                    
T = int(input())
for t in range(1,T+1):
    R,C = [int(x) for x in input().split()]
    cake = [input() for i in range(R)]
    cake = [list(x) for x in cake]

    cake = compute(cake)
    print("Case #%d:"%t)
    for r in cake:
        print("".join(r))

