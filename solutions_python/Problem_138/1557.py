# file_name = "D-small-attempt0"
file_name = "D-large"

f = open("../../../../" + file_name + ".in", "r")
# f = open("../test.txt")
w = open("../../../../" + file_name + ".out", "w")
TIMES = int(f.readline())

for T in range(1, TIMES + 1):
    print T
    w.write("Case #" + str(T) + ": ")
    f.readline()
    naomi = map(float, f.readline().split())
    ken = map(float, f.readline().split())
    win_normal, win_d = 0, 0
    ken_used = len(ken) * [False]
    ken_sorted = sorted(ken)
    for card in naomi:
        ken_win = False
        for ken_index in range(len(ken)):
            ken_card = ken_sorted[ken_index]
            if ken_card > card and not ken_used[ken_index]:
                ken_win = True
                ken_used[ken_index] = True
                break
        if not ken_win:
            win_normal += 1
            i = 0
            while ken_used[i]:
                i += 1
            ken_used[i] = True
    naomi_used = len(naomi) * [False]
    naomi_sorted = sorted(naomi)
    for card in ken_sorted:
        still_large_enough = False
        for naomi_index in range(len(naomi)):
            naomi_card = naomi_sorted[naomi_index]
            if naomi_card > card and not naomi_used[naomi_index]:
                still_large_enough = True
                naomi_used[naomi_index] = True
                win_d += 1
                break
    w.write(str(win_d) + " " + str(win_normal) + "\n")
        

            
            
    
    
        
    
    
