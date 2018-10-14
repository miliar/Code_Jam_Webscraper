num_cases = int(raw_input())

for case_no in xrange(1, num_cases+1):
    answer = people = 0
    tokenized = raw_input().split()
    max_shy, count_shy = int(tokenized[0]), map(int, tokenized[1])
    for level in xrange(0, max_shy+1):
        if level > people:
            answer += level - people
            people = level
        
        people += count_shy[level]

    print "Case #%d: %d" % (case_no, answer)