INPUT = "A-small-attempt0.in"
OUTPUT = "A-small-attempt0.out"


def OversizedPancakeFlipper(S, K):
    explored = {}
    possibles = []
    cnt = 0
    def solution(S, K, cnt):


        possibles.append(S)
        Slist = list(S)
        cnt += 1

        for i in range(len(Slist) - (K-1)):
            for j in range(K):
                if Slist[i+j] == "+":
                    Slist[i+j] = "-"
                else:
                    Slist[i+j] = "+"
            if "".join(Slist) in possibles:
                # print cnt
                cnt = explored.get("".join(Slist)) + 1
            else :
                explored.update({"".join(Slist):cnt})
                solution("".join(Slist),K,cnt)


    explored = { S:cnt}
    solution(S, K, cnt)
    # print explored
    if explored.get("+"*len(S)) == None:
        return ("IMPOSSIBLE")
    else:
        return str(explored.get("+"*len(S)))


with open(INPUT +".txt") as infile:
    with open(OUTPUT, 'w') as outfile:
        numCases = int(infile.readline())

        for i in range(numCases):

            S, K = infile.readline().split()
            # print S
            # print K
            outfile.write("Case #%d: %s\n" % (i + 1, OversizedPancakeFlipper(S, int(K))))