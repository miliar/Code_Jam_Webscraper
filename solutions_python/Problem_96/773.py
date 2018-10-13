
def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    line_num = int(data[0].strip())
    lines = [data[i].strip() for i in xrange(line_num + 1)]
    lines = lines[1:]
    assert len(lines) == line_num
    
    return lines
 
def calc_scores():
    """
    Calculation regular and special cases for all score sums
    """
    
    scores = []
    for i in xrange(31):
        reg = [i / 3] * 3
        for j in xrange(i % 3):
            reg[2 - j] = i / 3 + 1
            
        special = reg[:]
        if i % 3 != 2:
            special[0] -= 1
            special[1] += 1
            
            if special[0] < 0 or special[1] > 10:
                special = []
        else:
            special[1] -= 1
            special[2] += 1
            
            if special[1] < 0 or special[2] > 10:
                special = []
            
        scores.append([reg, special])
        
    return scores
    
def create_options(sums, specials, scores):
    """
    recursively yielding all choices
    """            
        
    # Yielding current specials
    x = [scores[sums[i]][0] if i not in specials else scores[sums[i]][1] for i in xrange(len(sums))]
    yield x
    
    if not specials:
        return
    
    new_specials = specials[:]
    new_specials[len(new_specials) - 1] += 1
    
    done = False
    while not done:
        all_good = True
        for i in xrange(len(new_specials)):
            if new_specials[i] >= len(sums):
                if i == 0:
                    return
                
                all_good = False
                for j in xrange(i, len(new_specials)):
                    new_specials[j] = 0
                new_specials[i - 1] += 1
        
        if all_good:
            done = True
            
    for i in create_options(sums, new_specials, scores):
        yield i
    
    
def calc_max(s, p, t, scores):
    """
    Calculation maximum Googlers who have points more than p, with s special cases and t the sum
    of their votes
    """
    
    # Creating all cases
    specials = range(s)
    score_options = create_options(t, specials, scores)
    max = 0
    for option in score_options:
        count = 0
        for player in option:
            if any(i >= p for i in player):
                count += 1
                
        if count > max:
            max = count
            
            if max == len(t):
                return max
            
    return max
    
def get_nums(lines):
    scores = calc_scores()
    
    nums = []
    for line in lines:
        print line
        x = line.split(' ')
        (n, s, p, t) = (int(x[0]), int(x[1]), int(x[2]), [int(i) for i in x[3:]])
        assert len(t) == n
        
        nums.append(calc_max(s, p, t, scores))
        
    return nums

def create_output(nums):
    with file('output1.txt', 'wt') as f:
        for (i, num) in enumerate(nums):
            print >> f, 'Case #%d: %d' % (i + 1, num) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    nums = get_nums(data)
    create_output(nums)

if __name__ == "__main__":
    main()