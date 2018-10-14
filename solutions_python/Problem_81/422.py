T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    teams = []
    for n in xrange(N):
        teams.append({
            'line': raw_input().rstrip(),
        })
    def wp(line, ignore=-1):
        cnt = 0
        sum = 0.0
        for i, ch in enumerate(line):
            if i == ignore: continue
            if ch != '.': cnt += 1
            if ch == '1': sum += 1
        return sum / cnt
    # WP
    for team in teams:
        team['wp'] = wp(team['line'])
    # OWP
    for i, team in enumerate(teams):
        cnt = 0
        sum = 0.0
        for j, ch in enumerate(team['line']):
            if ch != '.':
                cnt += 1
                sum += wp(teams[j]['line'], i)
        team['owp'] = sum / cnt
    for team in teams:
        cnt = 0
        sum = 0.0
        for i, ch in enumerate(team['line']):
            if ch != '.':
                cnt += 1
                sum += teams[i]['owp']
        team['oowp'] = sum / cnt
    print "Case #%d:" % (t + 1)
    for team in teams:
        print (team['wp'] * 0.25 +
               team['owp'] * 0.5 +
               team['oowp'] * 0.25)

