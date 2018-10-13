def wp(matrix):
    return map(lambda z: len(filter(lambda c:c=="1", z)) * 1.0 / len(filter(lambda c:c!=".", z)), matrix)

def owp(matrix, team):
    x = 0
    s = 0
    for opponent in range(len(matrix)):
        if matrix[team][opponent] == ".":
            continue
        x += len(filter(lambda c:c=="1", matrix[opponent][:team] + matrix[opponent][team+1:])) * 1.0 / len(filter(lambda c:c!=".", matrix[opponent][:team] + matrix[opponent][team+1:]))
        s += 1
    return x * 1.0 / s
    
def oowp(matrix, owps):
    oowps = []
    for team in range(len(matrix)):
        s = 0
        t = 0
        for opponent in range(len(matrix)):
            if matrix[team][opponent] != ".":
                s += owps[opponent]
                t += 1
        oowps.append(s * 1.0 / t)
    return oowps        
        
    
def rpi(matrix):
    wps = wp(matrix)
    owps = [owp(matrix, team) for team in range(len(matrix))]
    oowps = oowp(matrix, owps)
    return [0.25 * w + 0.5 * ow + 0.25 * oow for (w, ow, oow) in zip(wps, owps, oowps)]

def main():
    cases = int(raw_input())
    for case in range(cases):
        n = int(raw_input())
        matrix = []
        for i in range(n):
            matrix.append(raw_input())
        print "Case #%d:\n%s" % (case+1,  "\n".join(map(lambda n: ("%.8f" % n), rpi(matrix))))

main()

