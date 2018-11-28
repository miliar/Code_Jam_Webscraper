from sys import stderr, stdout

def solve_case(h, w, altitudes):
    flows_to = dict() # a:b -> water from a flows to b
    flows_from = dict() # a: [b, c, d] -> water from b, c, and d flow to a
    
    sinks = set()

    for square in altitudes.keys():
        # From which direction?
        min_alt = altitudes[square]
        to_square = 0
        # north?
        if square[0] > 0:
            to_candidate = (square[0] - 1, square[1])
            to_candidate_alt = altitudes[to_candidate]
            if to_candidate_alt < min_alt:
                min_alt = to_candidate_alt
                to_square = to_candidate
        # west?
        if square[1] > 0:
            to_candidate = (square[0], square[1] - 1)
            to_candidate_alt = altitudes[to_candidate]
            if to_candidate_alt < min_alt:
                min_alt = to_candidate_alt
                to_square = to_candidate

        # east?
        if square[1] < w - 1:
            to_candidate = (square[0], square[1] + 1)
            to_candidate_alt = altitudes[to_candidate]
            if to_candidate_alt < min_alt:
                min_alt = to_candidate_alt
                to_square = to_candidate

        # south?
        if square[0] < h - 1:
            to_candidate = (square[0] + 1, square[1])
            to_candidate_alt = altitudes[to_candidate]
            if to_candidate_alt < min_alt:
                min_alt = to_candidate_alt
                to_square = to_candidate

        if to_square == 0:
            # this is a sink
            sinks.add(square)
        else:
            # update the flow chart
            flows_to[square] = to_square

            if to_square not in flows_from:
                flows_from[to_square] = set()

            flows_from[to_square].add(square)

    #print >> stderr, "Flows to:", flows_to
    #print >> stderr, "Flows from:", flows_from    
    #print >> stderr, "Sinks:", sinks

    # Starting from sinks, update the "sink where flows" of all squares
    sink_to = dict()
    squares_to_process = set()
    for square in sinks:
        sink_to[square] = square
        if square in flows_from:
            squares_to_process.update(flows_from[square])

    while len(squares_to_process) > 0:
        square = squares_to_process.pop()
        sink_to[square] = sink_to[flows_to[square]]
        if square in flows_from:
            squares_to_process.update(flows_from[square])

    # Convert sink coordinates to sink id's
    sink_ids = dict()
    sink_letters = 0

    solution = dict()
    for row_ind in range(h):
        for col_ind in range(w):
            sink = sink_to[(row_ind, col_ind)]
            if sink not in sink_ids:
                sink_ids[sink] = chr(ord('a') + sink_letters)
                sink_letters += 1

            solution[(row_ind, col_ind)] = sink_ids[sink]

    return solution


if __name__ == '__main__':
    # Read the input
    no_maps = int(raw_input(''))

    for map_ind in range(no_maps):
        (h, w) = raw_input('').split(' ')
        h = int(h)
        w = int(w)
        altitudes = dict()

        for row_ind in range(h):
            row = raw_input('').split(' ')
            for col_ind in range(w):
                altitudes[(row_ind, col_ind)] = int(row[col_ind])

        #print >> stderr, altitudes

        print >> stderr, "Solving case %d" % (map_ind + 1)

        sol = solve_case(h, w, altitudes)

        print "Case #%d:" % (map_ind + 1)

        for row_ind in range(h):
            for col_ind in range(w):
                stdout.write('%s ' % sol[(row_ind, col_ind)])
            stdout.write('\n')


