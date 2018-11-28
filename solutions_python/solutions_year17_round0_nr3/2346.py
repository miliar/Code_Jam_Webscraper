from collections import deque

def main():
    """ Using a queue this time """
    t = int(raw_input())

    for i in range(t):
        n, k = raw_input().split()
        n = int(n)
        k = int(k)

        if n == k:
            print "Case #"+str(i+1)+":", 0, 0
            continue

        queue = deque([(0, n+1)])
        done = False
        count = 0
        for j in range(k):
            small = []
            big = []
            while queue:
                pair = queue.popleft()
                mid = (pair[0] + pair[1]) // 2
                fhalf, fdiff = (pair[0], mid), mid - pair[0] - 1
                shalf, sdiff = (mid, pair[1]), pair[1] - mid - 1
                #print pair, fhalf, shalf
                count += 1
                if fdiff >= sdiff:
                    big.append(fhalf)
                    small.append(shalf)
                else:
                    big.append(shalf)
                    small.append(fhalf)

                if count == k:
                    print "Case #"+str(i+1)+":", max(fdiff, sdiff), min(fdiff, sdiff)
                    done = True
                    break
            if done:
                break
            

            queue.extend(big)
            queue.extend(small)
