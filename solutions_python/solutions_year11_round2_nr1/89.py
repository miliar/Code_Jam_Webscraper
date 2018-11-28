t = int(input())
for i in range(t):
    n = int(input())
    win_data = []
    for j in range(n):
        win_data.append(input())
    wp = n*[0]
    wp1 = n*[0] # wp minus one win
    wp2 = n*[0] # wp minus one loss
    for j in range(n):
        played = 0
        won = 0
        for k in range(n):
            if win_data[j][k] == '1':
                played+=1
                won+=1
            elif win_data[j][k] == '0':
                played+=1
        wp[j] = float(won)/played
        wp1[j] = float(won-1)/(played-1)
        wp2[j] = float(won)/(played-1)
    owp = n*[0]
    for j in range(n):
        played = 0
        total = 0
        for k in range(n):
            if win_data[j][k] == '1':
                played += 1
                total += wp2[k]
            elif win_data[j][k] == '0':
                played += 1
                total += wp1[k]
        owp[j] = total/played
    oowp = n*[0]
    for j in range(n):
        played = 0
        total = 0
        for k in range(n):
            if win_data[j][k] == '1' or win_data[j][k] == '0':
                played += 1
                total += owp[k]
        oowp[j] = total/played
    rpi = n*[0]
    print("Case #%d:" % (i+1))
    for j in range(n):
        print(0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j])
