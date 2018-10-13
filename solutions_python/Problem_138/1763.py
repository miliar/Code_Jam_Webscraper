def get_ken_move(naomi, kens):
    if naomi > max(kens):
        return min(kens)
    else:
        return min([b for b in kens if b > naomi])

def get_legal_moves_for_war(naomis, kens):
    moves_by_k = {}
    for n in naomis:
        k = get_ken_move(n, kens)
        if k in moves_by_k:
            if n < moves_by_k[k]:
                moves_by_k[k] = n
        else:
            moves_by_k[k] = n
    return [(n, k) for k, n in moves_by_k.iteritems()]

def get_legal_moves_for_deceitful_war(naomis, kens):
    moves = set()
    min_k = min(kens)
    max_k = max(kens)
    min_n = min(naomis)
    moves.add((min_n, min_k))
    if max_k > min_n:
        moves.add((min_n, max_k))
    # for n in naomis:
    #     # for k in [k for k in kens if k > n]:
    #     #     moves.add((n, k))
    #     if max_k > n:
    #         moves.add((n, max_k))
    return moves

def get_point(naomis, kens, move_generator):
    if len(naomis) == 1:
        return 1 if list(naomis)[0] > list(kens)[0] else 0
    points = []
    for move in move_generator(naomis, kens):
        point_of_move = (1 if move[0] > move[1] else 0)
        # print naomis, kens, move, point_of_move
        points.append(point_of_move + get_point(naomis - set([move[0]]), kens - set([move[1]]), move_generator))
    return max(points)

# print get_point_for_war(set([0.5, 0.1, 0.9]), set([0.6, 0.4, 0.3]), get_legal_moves_for_war)
# print get_point_for_war(set([0.5, 0.1, 0.9]), set([0.6, 0.4, 0.3]), get_legal_moves_for_deceitful_war)
# print get_legal_moves_for_war(set([0.5, 0.1, 0.9]), set([0.6, 0.4, 0.3]))

sample_count = int(raw_input())
for i in xrange(1, sample_count + 1):
    block_count = int(raw_input())
    naomis = set([float(s) for s in raw_input().split(' ')])
    kens = set([float(s) for s in raw_input().split(' ')])
    print "Case #%d: %d %d" % (i, get_point(naomis, kens, get_legal_moves_for_deceitful_war), get_point(naomis, kens, get_legal_moves_for_war))
