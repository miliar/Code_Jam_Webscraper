from string import maketrans

def get_result(answer1, arrangement1, answer2, arrangement2):
    shared_cards = set(arrangement1[answer1-1]) & set(arrangement2[answer2-1])
    if len(shared_cards) == 1:
        return shared_cards.pop()
    elif shared_cards:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        T = int(f.readline().strip())
        for i in range(T):
            answer1 = int(f.readline().strip())
            arrangement1 = []
            for j in range(4):
                arrangement1.append(f.readline().strip().split())
            answer2 = int(f.readline().strip())
            arrangement2 = []
            for j in range(4):
                arrangement2.append(f.readline().strip().split())
            result = get_result(answer1, arrangement1, answer2, arrangement2)
            print 'Case #%d: %s'%(i+1, result)
            
