precalc = [["   1","  12","   1","  12"], 
           ["  12","  12"," 123","  12"], 
           ["   1"," 123","  13","1234"], 
           ["  12","  12","1234"," 124"], 
]

for t in range(int(input())):
    x, r, c = map(int, input().split())
    print("Case #", t + 1, ": ", ("GABRIEL" if str(x) in precalc[r - 1][c - 1] else "RICHARD"), sep = "")
