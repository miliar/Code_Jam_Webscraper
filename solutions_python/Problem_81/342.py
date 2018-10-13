#!/usr/bin/python

import sys

def main():
    if len(sys.argv) < 3:
        print "Needs input and output files"
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')

    cases = int(fin.readline())

    for c in range(cases):
        num_teams = int(fin.readline())
        mat = []
        
        for team in range(num_teams):
            s = fin.readline().strip()                   
            mat.append(list(s))
        
        wp = []
        games_played = []
        opponents = []
        
        for team in mat:
            wp_val = 0.0
            games = 0.0
            ops = []
            for i in range(len(team)):
                char = team[i]
                if char != '.':
                    ops.append(i)
                    if char == '1':
                        wp_val += 1
                    games += 1
            wp.append(wp_val)
            games_played.append(games)
            opponents.append(ops)
        
        owp = []
        
        for i in range(num_teams):
            owp_total = 0.0
            num_ops = 0.0
            for op in opponents[i]:
                num_ops += 1
                owp_val = wp[op] - float(mat[op][i])
                owp_val /= (games_played[op] - 1)
                owp_total += owp_val
            owp.append(owp_total / num_ops)
        
        oowp = []
        
        for i in range(num_teams):
            oowp_total = 0.0
            num_ops = 0.0
            for op in opponents[i]:
                oowp_total += owp[op]
                num_ops += 1
            oowp.append(oowp_total / num_ops)   
        
        fout.write("Case #%d:\n" % (c + 1)) 
        for i in range(num_teams):
            rpi = 0.25 * (wp[i] / games_played[i]) + 0.5 * owp[i] + 0.25 * oowp[i]
            fout.write(str(rpi) + "\n")

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()