
num = input()

for testnum in range(num):
    d = map(list,[raw_input(), raw_input(), raw_input(), raw_input()])
    if testnum+1<num:
        raw_input()
    diags = [[d[i][i] for i in range(4)], [d[i][3-i] for i in range(4)]]
    x = any([all([l in "XT" for l in ll]) for ll in d+zip(*d)+diags])
    o = any([all([l in "OT" for l in ll]) for ll in d+zip(*d)+diags])
    full = not any(['.' in l for l in d])
    print "Case #%i: %s"%(testnum+1, {
        (False,False):"Draw" if full else "Game has not completed",
        (True,False):"X won",
        (False,True):"O won",
        }[(x,o)])
    
    
    
    

