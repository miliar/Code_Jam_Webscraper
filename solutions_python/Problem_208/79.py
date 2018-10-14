#!/usr/bin/env pypy

INF = 10 ** 100

num_tests = input()

for test_no in xrange(1, num_tests + 1):
    n_cities, n_questions = map(int, raw_input().split())
    endurance, speed = [], []
    for i in xrange(n_cities):
        e, s = map(int, raw_input().split())
        endurance.append(e)
        speed.append(s)
    dist = []
    for i in xrange(n_cities):
        dist.append(map(int, raw_input().split()))
    questions = []
    for i in xrange(n_questions):
        questions.append(map(int, raw_input().split()))

    question_answers = []
    for global_source, global_dest in questions:
        global_source -= 1
        global_dest -= 1

        arrival = [INF] * n_cities
        arrival[global_source] = 0.
        
        reachable = [False] * n_cities
        reachable[global_source] = True

        completed = [False] * n_cities
        
        while True:
            source = None
            for c in xrange(n_cities):
                if not completed[c] and reachable[c] and (source is None or arrival[c] < arrival[source]):
                    source = c
            if source == global_dest:
                break
            
            hend = endurance[source]
            hspeed = speed[source]

            reachable2 = [False] * n_cities
            reachable2[source] = True
            
            completed2 = [False] * n_cities
            
            total_dist = [INF] * n_cities
            total_dist[source] = 0.
            
            while True:
                source2 = None
                for c in xrange(n_cities):
                    if not completed2[c] and reachable2[c] and (source2 is None or total_dist[c] < total_dist[source2]):
                        source2 = c
                if source2 is None or source2 == global_dest:
                    break
                
                for d in xrange(n_cities):
                    #print source2
                    if dist[source2][d] == -1:
                        continue
                    tdist = total_dist[source2] + dist[source2][d]
                    if tdist > hend:
                        continue

                    total_dist[d] = min(total_dist[d], tdist)
                    arrival[d] = min(arrival[d], arrival[source] + total_dist[d] / hspeed)
                    
                    reachable[d] = reachable2[d] = True
                
                completed2[source2] = True

            completed[source] = True
            
        question_answers.append(arrival[global_dest])
        
    """    arrival = [INF] * n_cities
    arrival[questions[0][0] - 1] = 0
    for source in xrange(questions[0][0] - 1, questions[0][1] - 1):
        hspeed = speed[source]
        hend = endurance[source]
        total_dist = 0.
        for dest in xrange(source + 1, questions[0][1]):
            total_dist += dist[dest-1][dest]
            if total_dist > hend:
                break
            arrival[dest] = min(arrival[dest], arrival[source] + total_dist / hspeed)

    print 'Case #{0}: {1}'.format(test_no, arrival[questions[0][1] - 1])"""
    
    print 'Case #{0}: {1}'.format(test_no, ' '.join(map(str, question_answers)))
