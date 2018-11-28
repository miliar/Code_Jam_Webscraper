def lire(path) :
    test = open(path, "r")
    liste = []
    long = int(test.readline())
    for c in test.readlines():
        ligne = c.rstrip()
        liste.append(ligne)
    test.close()
    return liste



def t_f(x0,L,v):
    return (L-x0)/v

def sol(nb, L, entree) :
    t = [0]*nb
    for i in range(nb):
        x0, v = map(int, entree.readline().rstrip().split())
        t[i] = t_f(x0,L, v)
    t_max = max(t)
    return L/t_max


def main():
    path = "A-small-attempt0.in.txt"
    entree = open(path, "r")
    nb_case = int(entree.readline())
    rep = open("Cruise_Control_small_O.txt", "w")
    for i in range(1, nb_case+1):
        L, nb = map(int, entree.readline().rstrip().split())
        rep.write("Case #" + str(i)+": " + str(sol(nb, L, entree))+"\n")

    rep.close()
    
