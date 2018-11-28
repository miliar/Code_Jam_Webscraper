reader = open('A-large.in')
writer = open('output-large', 'w')

test_cases = int(reader.readline())

def WP(arr, n, omit = -1):
    wins = 0
    losses = 0

    for a in range(len(arr[n])):
        if a == omit:
            pass
        else:
            if arr[n][a] == 0:
                losses += 1
            elif arr[n][a] == 1:
                wins += 1

    if losses == 0:
        if wins == 0:
            return 0
        else:
            return 1
    else:
        return float(wins) / (wins + losses)

def OWP(arr, n):
    count = 0
    wp_total = 0
    
    for a in range(len(arr[n])):
        if arr[n][a] >= 0: # they are an opponent
            wp_total += float(WP(arr, a, n))
            count += 1

    return wp_total / float(count)

def OOWP(arr, n):
    count = 0
    owp_total = 0
    
    for a in range(len(arr[n])):
        if arr[n][a] >= 0: # they are an opponent
            owp_total += float(OWP(arr, a))
            count += 1

    return owp_total / float(count)

for i in range(test_cases):
    writer.write('Case #%s:' % (i + 1) + '\n')
    width = int(reader.readline())
    matches = []
    for row in range(width):
        a = []
        row = list(reader.readline()[:-1])
        for char in row:
            if char == '.':
                a.append(-1)
            else:
                a.append(int(char))
        matches.append(a)

    for team in range(width):
        writer.write(str(0.25 * WP(matches, team) + 0.50 * OWP(matches, team) + 0.25 * OOWP(matches, team)) + '\n')

reader.close()
writer.close()

        
        
