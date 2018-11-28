import numpy as np
from dijkstar import Graph, find_path


def crea_matrice_distanze(dist):
    initial_matr = np.array(dist)
    print initial_matr
    matr = initial_matr.copy()
    # dict_matr = {(partenza, arrivi): lunghezza for partenza, arrivi in enumerate(dist) for arrivo, lunghezza in
    #              enumerate(arrivi)}
    graph = Graph()

    for partenza, arrivi in enumerate(dist):
        for arrivo, lunghezza in enumerate(arrivi):
            if lunghezza >= 0:
                graph.add_edge(partenza, arrivo, {'cost': lunghezza})
    cost_func = lambda u, v, e, prev_e: e['cost']

    for partenza, arrivi in enumerate(dist):
        for arrivo in range(len(arrivi)):
            if partenza == arrivo:
                matr[partenza, arrivo] = -1
            else:
                try:
                    min_dist = find_path(graph, partenza, arrivo, cost_func=cost_func)[3]
                    matr[partenza, arrivo] = min_dist
                except Exception as e:
                    matr[partenza, arrivo] = -1
    print "matr ditanze\n", matr
    return matr



def crea_grafo(min_dist_matr, cavalli):
    matr = min_dist_matr.copy()
    for partenza, cavallo in enumerate(cavalli):
        c_endurance = cavallo["endurance"]
        c_speed = cavallo["speed"]
        # print "cavallo", cavallo
        # print "dist cavallo", min_dist_matr[partenza]
        for arrivo, lunghezza in enumerate(min_dist_matr[partenza]):
            # print "p a l s v",  partenza, arrivo, lunghezza, c_speed, 1.0 * float(lunghezza) / c_speed
            if lunghezza > -1 and lunghezza <= c_endurance:
                matr[partenza, arrivo] = 1.0 * float(lunghezza) / c_speed
                print matr[partenza, arrivo]
            else:
                matr[partenza, arrivo] = -1

    # print "matr cavallo \n", matr
    graph = Graph()

    for partenza, arrivi in enumerate(matr):
        for arrivo, lunghezza in enumerate(arrivi):
            if lunghezza >= 0:
                graph.add_edge(partenza, arrivo, {'cost': lunghezza})
    return graph


def min_path_cavallo(graph_ottimo, tratta):
    tratta_partenza = tratta["partenza"]
    tratta_arrivo = tratta["arrivo"]
    cost_func = lambda u, v, e, prev_e: e['cost']
    try:
        res_dist = find_path(graph_ottimo, tratta_partenza - 1, tratta_arrivo - 1, cost_func=cost_func)[3]
        # matr[partenza, arrivo] = res_dist
    except Exception as e:
        res_dist = -1
        print e
    return res_dist

def solve(mhorses, mdistances, mtratte):
    matr_dist = crea_matrice_distanze(dist=mdistances)
    graph_tratte = crea_grafo(min_dist_matr=matr_dist, cavalli=mhorses)
    res_list = []
    for tratta in mtratte:
        res_list.append(min_path_cavallo(graph_ottimo=graph_tratte, tratta=tratta))
    return res_list



risultati = []
with open("C-small-attempt0.in") as f:
    t = int(f.readline())
    print "t", t
    for i in range(t):
        n, q = [int(x) for x in f.readline().strip().split(" ")]
        print "n, q", (n, q), i
        horses = []
        for j in range(n):
            e, s = [int(x) for x in f.readline().strip().split(" ")]
            horses.append({"endurance": e, "speed": s})

        distances = []
        for j in range(n):
            dj = [int(x) + 0.0 for x in f.readline().strip().split(" ")]
            distances.append(dj)

        tratte = []
        for j in range(q):
            u, v = [int(x) for x in f.readline().strip().split(" ")]
            tratte.append({"partenza": u, "arrivo": v})

        print horses
        print distances
        print tratte

        # print row
        risultati.append(solve(mhorses=horses, mdistances=distances, mtratte=tratte))

with open("outSmall.txt", "w") as out:
    for i, r in enumerate(risultati):
        out.write("Case #{}: {}\n".format(i+1, " ".join(str(x) for x in r)))
