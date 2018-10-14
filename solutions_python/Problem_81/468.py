#RPI problem
start_of_case = True
case_size = []
case_grid = []
case_double_grid = []
games_played = []
full_games_played = []
WP = []
full_WP = []
OWP = []
full_OWP = []
OOWP = []
full_OOWP =[]
x = 0
i = 0
game_amount = 0
file_ = open('A-large.txt','r')
for line in file_:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        if(start_of_case):
            case_size.append(int(line))
            start_of_case = False
            temp = i
        else:
            game_amount = 0
            if(i - temp <= case_size[x]):
                WP.append(0)
                OWP.append(0)
                OOWP.append(0)
                for letters in line:
                    if letters != '\n':
                        if letters != '.':
                            game_amount = game_amount + 1
                            case_grid.append(int(letters))
                        else:
                            case_grid.append(2)
                games_played.append(game_amount)

                if(i - temp == case_size[x]):
                    x = x + 1
                    start_of_case = True
                    case_double_grid.append(case_grid)
                    case_grid = []
                    full_games_played.append(games_played)
                    full_WP.append(WP)
                    full_OWP.append(OWP)
                    full_OOWP.append(OOWP)
                    WP = []
                    OWP = []
                    OOWP = []
                    games_played = []

for x in range(0,total_cases):
    print "Case #{0}:" .format(x+1)
    for y in range(0,len(case_double_grid[x]),case_size[x]):
        total_won = 0.0
        for z in range(0,case_size[x]):
            if (case_double_grid[x][y+z] == 1):
                total_won = total_won + 1
        full_WP[x][y/case_size[x]] = total_won/full_games_played[x][y/case_size[x]]

    for A in range(0,case_size[x]):
        OWP_precentages = []
        for B in range(0,case_size[x]):
            if(case_double_grid[x][B*case_size[x] + A] != 2):
                OWP_games_played = 0.0
                OWP_games_won = 0.0
                for C in range(0,case_size[x]):
                    if(C != A):
                        if (case_double_grid[x][B*case_size[x]+C] != 2):
                            OWP_games_played = OWP_games_played + 1
                        if (case_double_grid[x][B*case_size[x]+C] == 1):
                            OWP_games_won = OWP_games_won + 1

                OWP_precentages.append(OWP_games_won/OWP_games_played)
        OWP_temp = 0
        for D in range (0,len(OWP_precentages)):
            OWP_temp = OWP_temp + OWP_precentages[D]

        OWP_temp = OWP_temp/len(OWP_precentages)
        full_OWP[x][A] = OWP_temp

    for A in range(0,case_size[x]):
        OOWP_temp = 0
        OOWP_size = 0
        for B in range(0,case_size[x]):
            if(case_double_grid[x][B*case_size[x] + A] != 2):
                OOWP_temp = OOWP_temp + full_OWP[x][B]
                OOWP_size = OOWP_size + 1
        OOWP_temp = OOWP_temp / OOWP_size
        full_OOWP[x][A] = OOWP_temp

    for A in range(0,case_size[x]):
        solution = .25*full_WP[x][A] + .5*full_OWP[x][A] + .25*full_OOWP[x][A]
        print solution
