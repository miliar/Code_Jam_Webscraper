#!/usr/bin/env python

def main():
    f = open('input.txt')

    total_T = int(f.readline())

    for T in xrange(1,total_T+1):
        #print T
        N,M = f.readline().rstrip('\n').split()
        N,M=int(N),int(M)
        map_ = [[] for asd in xrange(N)]
        for line_c in xrange(N):
            asd = f.readline().rstrip('\n')
            asd = asd.split()
            map_[line_c] = asd
        
        is_Yes = 1
        for i in xrange(N):
            for j in xrange(M):
                if not check_item(i,j,map_,N,M):
                    is_Yes = 0

        if is_Yes:
            print "Case #{}: YES".format(T)
        else:
            print "Case #{}: NO".format(T)


def check_item(i,j,map_, N,M):
    if all([map_[asd][j] <= map_[i][j] for asd in xrange(N)]):
        return True
    if all([map_[i][asd] <= map_[i][j] for asd in xrange(M)]):
        return True

    return False

if __name__ == '__main__':
    main()