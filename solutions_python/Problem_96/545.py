


def nrOfBest(n, points, suprises, best):
    count, points = nrOfBestNoSuprise(points, best)
    if suprises > 0:
        points.sort(reverse=True)
        minp = best - 2
        if minp < 0 : minp = 0
        for point in points:
            remtwo = (point - best)
            if remtwo < 0:
                break
            rem  = remtwo - 2*(best - 2)
            if rem >= 0:
                count += 1
                suprises -= 1
                if suprises == 0:
                    break
    return count

def nrOfBestNoSuprise(points, best):
    count = 0
    rempoints = []
    minp = best - 1
    if min < 0 : minp = 0
    for point in points:
        remtwo = (point - best)
        if remtwo < 0:
            rempoints.append(point)
            continue
        rem = remtwo - 2* (minp)
        if rem >= 0:
            count += 1
        else:
            rempoints.append(point)
    return (count, rempoints)

if __name__ == '__main__':
    f = open("input.txt")
    out = open("output.txt", "w")
    nr = int(f.readline())
    
    for i in range(1, nr + 1):
        problem = f.readline().strip().split()
        n = int(problem[0])
        suprises = int(problem[1])
        best = int(problem[2])
        points = [int(p) for p in problem[3:]]
        sollution = nrOfBest(n, points, suprises, best)
        
        s = "Case #" + str(i) + ": " + str(sollution)
        print s
        out.write(s + "\n")

    out.close()
    f.close()