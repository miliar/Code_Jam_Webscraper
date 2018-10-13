def calculate_wp(all_teams, team, N):
    sum = 0
    count = 0
    for other_team in xrange(N):
        if all_teams[team][other_team] == '1':
            sum += 1
            count += 1
        elif all_teams[team][other_team] == '0':
            count += 1

    return sum/float(count)

def calculate_wp_without_index(all_teams, team, N, index):
    sum = 0
    count = 0
    for other_team in xrange(N):
        if other_team == index:
            continue
        if all_teams[team][other_team] == '1':
            sum += 1
            count += 1
        elif all_teams[team][other_team] == '0':
            count += 1

    return sum/float(count)
    
def calculate_owp(all_teams, team, N):
    sum = 0
    count = 0
    for other_team in xrange(N):
        if all_teams[team][other_team] is not None:
            sum += calculate_wp_without_index(all_teams, other_team, N, team)
            count += 1
    return sum/float(count)
    
    

def calculate_oowp(all_teams, team, N):
    sum = 0
    count = 0
    for other_team in xrange(N):
        if all_teams[team][other_team] is not None:
            sum += calculate_owp(all_teams, other_team, N)
            count += 1
    return sum/float(count)
    

input_file = file('input.txt', 'rb')
out_file = file('output.txt', 'wb')
lines = input_file.readlines()
T = int(lines[0])
current_line = 1
for index in xrange(0, T):
    out_file.write("Case #%s:\n" % str(index+1))
    N = int(lines[current_line])
    current_line += 1
    all_teams = []
    for team in xrange(0,N):
        temp_line = lines[current_line]
        all_teams.append([])
        for current_char in temp_line:
            if current_char == '.':
                all_teams[team].append(None)
            else:
                all_teams[team].append(current_char)
        current_line += 1

    for team in xrange(0,N):
        WP = calculate_wp(all_teams, team, N)
        OWP = calculate_owp(all_teams, team, N)
        OOWP = calculate_oowp(all_teams, team, N)
        RPI = 0.25 * WP + 0.5 * OWP + 0.25 * OOWP
        out_file.write("%12f\n" % (RPI))

    
out_file.close()
input_file.close()

    
    
