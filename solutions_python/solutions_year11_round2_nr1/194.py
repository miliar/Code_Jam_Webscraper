#-*- encoding: utf-8 -*-
import sys

def solve():
    return 0

if '__main__' == __name__:
    T = int(sys.stdin.readline())
    for case_n in xrange(T):
        N = int(sys.stdin.readline())
        team_info = [{} for _ in xrange(N)]
        team_data = [None for _ in xrange(N)]

        for team_n in xrange(N):
            team_data[team_n] = sys.stdin.readline().strip()
            for oppo_n, result in enumerate(team_data[team_n]):
                if '.' == result:
                    continue
                team_info[team_n].setdefault('WP', []).append(int(result))
            d = team_info[team_n].get('WP', [])
            WP = 0
            if d:
                WP = float(sum(d))/len(d)
            team_info[team_n]['WP'] = WP

        for drop_n in xrange(N):
            #print drop_n
            _team_info = [{} for _ in xrange(N)]
            for team_n in xrange(N):
                for oppo_n, result in enumerate(team_data[team_n]):
                    if '.' == result or drop_n==oppo_n:
                        continue
                    _team_info[team_n].setdefault('OWP', []).append(int(result))
                d = _team_info[team_n].get('OWP', [])
                OWP = 0
                if d:
                    OWP = float(sum(d))/len(d)
                team_info[drop_n].setdefault('OWP', []).append(OWP)
            d = team_info[drop_n].get('OWP', [])
            OPWs = []
            for oppo_n, result in enumerate(team_data[drop_n]):
                if '.' == result:
                    continue
                OPWs.append(d[oppo_n])
            OPW = 0.0
            if OPWs:
                OWP = float(sum(OPWs))/len(OPWs)
            team_info[drop_n]['OWP'] = OWP

        for team_n in xrange(N):
            data = []
            for oppo_n, result in enumerate(team_data[team_n]):
                if '.' == result:
                    continue
                data.append(team_info[oppo_n]['OWP'])
            OOWP = 0
            if data:
                OOWP = float(sum(data))/len(data)
            team_info[team_n]['OOWP'] = OOWP
            team_info[team_n]['RPI'] = 0.25*team_info[team_n]['WP'] + 0.50*team_info[team_n]['OWP'] + 0.25*team_info[team_n]['OOWP']


        #for idx, info in enumerate(team_info):
        #    print idx, team_data[idx], info

        print('Case #%d:' % (case_n+1))
        for data in team_info:
            print data['RPI']
