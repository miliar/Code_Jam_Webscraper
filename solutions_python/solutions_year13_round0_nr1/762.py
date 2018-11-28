wins = [
    (0,1,2,3),
    (4,5,6,7),
    (8,9,10,11),
    (12,13,14,15),
    (0,4,8,12),
    (1,5,9,13),
    (2,6,10,14),
    (3,7,11,15),
    (0,5,10,15),
    (3,6,9,12)
]

def check(trial,replacement):
    trial = trial.replace('T',replacement)
    for win in wins:
        if all([trial[win[x]] == replacement for x in range(4)]):
            return True
    return False

data = open(r"C:\Users\Eric\Desktop\data.txt").readlines()[1:]
case = 1
for i in range(0,len(data),5):
    trial = data[i:i+4]
    trialtext = "".join(trial).replace('\n','')
    if check(trialtext, 'X'):
        print 'Case #%d: %s' % (case,"X won")
    elif check(trialtext, 'O'):
        print 'Case #%d: %s' % (case,"O won")
    elif '.' in trialtext:
        print 'Case #%d: %s' % (case,"Game has not completed")
    else:
        print 'Case #%d: %s' % (case,"Draw")
    case += 1
