'''
I was in an airplane yesterday, so I couldn't compete on Draw Mohammed Day.
But I have something to make up for it!
Draw Mohammed Day 2011 Strikes Back!!!

Anyone who says I should not draw Mohammed can fuck off!
I am not a Muslim. I do not have to obey Islamic rules.
All religions can be criticised. Islam is not an exception.
Islam is not perfect.
When someone criticises Islam,
Muslims should either fix their mistakes or get used to the criticism.
Muslims should not try to scare their critics into submission.
Critics should not submit to threats of violence.
The state of freedom in this world is high enough
for people to not be scared of doing something
as vanilla as criticising a religion.

     ________________
    /___________/   /\
   /  DERKA        /  \
  /_______________/   /\
 /___/  \   \________/__\
/       /\    DERKA      \
|______/  \______________|
|     \    \_____________|
|     /\    MOHAMMED     |
|____/__\________________|
 |   XXXX        XXXX   |
 |   /O \        / O\   |
 |   \__/   /\   \__/   |
 |         |  |         |
 |         /__\         |
 |      XXXXXXXXXX      |
 \     XX ______ XX     /
  \   XX /      \ XX   / 
   \     |JIHAD!|     /
    \    \______/    /
     \      XX      /
      \  XXXXXXXX  /
       XXXXXXXXXXXX
        XXXXXXXXXX
         XXXXXXXX
          XXXXXX
                       ____
                      / -- \
                      ||__||
                      |    |
                      | __ |
                      | -- |
                      |    |
                      |    |
                      | __ |
                 ____ | -- | ____ 
                / -- \|    |/ -- \
                |    ||    ||    | ___ 
   ___          |    ||/  \||    |/ - \
  / --\         |/  \| |  | |/  \||   |
  ||  \\        ||  |  \  /  |  | |   |
  \\__/ \       |\  /        \  / |   \
   \     \      |                  / \ \
    \  /  \     |    DERKA DERKA   \ / |
     \// | \    |   MOHAMMED JIHAD     |
      \_/   \__/                       |
       \                               |
        \                              /
         \                            /
          \                          /
           \                        /
'''

def output(f, solution_iter):
    s = list()
    for solution in solution_iter:
        s.append('Case #')
        s.append(str(solution['number']))
        s.append(':\n')
        for rpi_element in solution['rpi_array']:
            s.append(str(rpi_element))
            s.append('\n')
    f.write(''.join(s))
    pass

def read(f):
    fiter = iter(f)
    cases = int(next(fiter))
    raw_problem_iter = list()
    for x in range(cases):
        player_count = int(next(fiter))
        game_array = list()
        for y in range(player_count):
            game_array.append(next(fiter).rstrip('\n'))
        raw_problem_iter.append({
            'number': x + 1,
            'game_array': game_array,
        })
        pass
    return iter(raw_problem_iter)

win_map = {
    '.': 0,
    '1': 1,
    '0': 0,
}

loss_map = {
    '.': 0,
    '1': 0,
    '0': 1,
}

def convert(raw_problem):
    play_tuple_array = list()
    for game in raw_problem['game_array']:
        win = list()
        loss = list()
        for symbol in game:
            win.append(win_map[symbol])
            loss.append(loss_map[symbol])
        play_tuple_array.append((win, loss))
    return {
        'number': raw_problem['number'],
        'play_tuple_array': play_tuple_array,
    }

def rpi(wp, owp, oowp):
    return float(wp + owp + owp + oowp) / 4

def winloss(play_tuple):
    win = sum(play_tuple[0])
    loss = sum(play_tuple[1])
    return win, win + loss, float(win) / (win + loss)

def calc_mwp(win, total, play_tuple, competitor_index):
    if play_tuple[0][competitor_index]:
        return float(win - 1) / (total - 1)
    else:
        if play_tuple[1][competitor_index]:
            return float(win) / (total - 1)
        else:
            return float(win) / total

def calc_oowp(owp_sum, owp_array, competitor_index, competitor_count_m1):
    return float(owp_sum - owp_array[competitor_index]) / competitor_count_m1

def solution(problem):
    player_count = len(problem['play_tuple_array'])
    win_list = list()
    total_list = list()
    wp_list = list()
    for play_tuple in problem['play_tuple_array']:
        win, total, wp = winloss(play_tuple)
        win_list.append(win)
        total_list.append(total)
        wp_list.append(wp)
    owp_list = list()
    pta = problem['play_tuple_array']
    for x in range(player_count):
        mwp_sum = 0
        competitor_count = 0
        for y in range(player_count):
            if (x != y) and (pta[x][0][y] or pta[x][1][y]):
                competitor_count += 1
                win = win_list[y]
                total = total_list[y]
                play_tuple = problem['play_tuple_array'][y]
                bla = calc_mwp(win, total, play_tuple, x)
                mwp_sum += bla
        owp_list.append(float(mwp_sum) / competitor_count)
    oowp_list = list()
    for x in range(player_count):
        oowp_sum = 0
        competitor_count = 0
        for y in range(player_count):
            if (x != y) and (pta[x][0][y] or pta[x][1][y]):
                competitor_count += 1
                oowp_sum += owp_list[y]
        oowp_list.append(float(oowp_sum) / competitor_count)
    rpi_array = list()
    for x in range(player_count):
        rpi_array.append(rpi(wp_list[x], owp_list[x], oowp_list[x]))
    solu = dict()
    solu['rpi_array'] = rpi_array
    solu['number'] = problem['number']
    return solu

def frame(in_file_path, out_file_path):
    solist = list()
    for raw_problem in read(open(in_file_path)):
        p = convert(raw_problem)
        s = solution(p)
        solist.append(s)
        pass
    output(open(out_file_path, 'w'), iter(solist))
    pass
