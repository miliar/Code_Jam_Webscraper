def read(f):
    return f.readline().strip()
with open("D-large.in") as infile:
    t = int(read(infile))
    for case in range(1,t+1):
        n = int(read(infile))
        deceit_wins = 0
        real_wins = 0
        line1 = read(infile).split()
        line2 = read(infile).split()


        naomi_blocks = sorted(list(map(float,line1)))
        ken_blocks = sorted(list(map(float,line2)))
        for rnd in range(n):
            chosen_naomi = naomi_blocks.pop()
            if any(x > chosen_naomi for x in ken_blocks):
                chosen_ken = min(x for x in ken_blocks if x > chosen_naomi)
            else:
                chosen_ken = min(ken_blocks)
                real_wins += 1
            ken_blocks.pop(ken_blocks.index(chosen_ken))


        naomi_blocks = sorted(list(map(float,line1)))
        ken_blocks = sorted(list(map(float,line2)))
        for rnd in range(n):
            if max(naomi_blocks) > max(ken_blocks):
                chosen_ken = ken_blocks.pop(ken_blocks.index(min(ken_blocks)))
                chosen_naomi = min(x for x in naomi_blocks if x > chosen_ken)
                naomi_blocks.pop(naomi_blocks.index(chosen_naomi))
                deceit_wins += 1
            else:
                chosen_naomi = naomi_blocks.pop(naomi_blocks.index(min(naomi_blocks)))
                chosen_ken = ken_blocks.pop(ken_blocks.index(max(ken_blocks)))
            
        print("Case #{}: {} {}".format(case, deceit_wins, real_wins))

