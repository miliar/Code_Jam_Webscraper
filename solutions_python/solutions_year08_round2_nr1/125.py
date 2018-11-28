
class CropField:

    def __init__(self, n, A, B, C, D, x0, y0, M):
        self.trees = []
        X = x0
        Y = y0
        self.trees.append(complex(X,  Y))
        for i in xrange(n-1):
          X = (A * X + B) % M
          Y = (C * Y + D) % M
          self.trees.append(complex(X,  Y))

    def number_of_triangles(self):
        triangles = 0
        for i in xrange(len(self.trees)-2):
            for j in xrange(i+1,  len(self.trees)-1):
                for k in xrange(j+1,  len(self.trees)):
                    center = (self.trees[i]+self.trees[j]+self.trees[k])/3
                    if center.real % 1 == 0 and center.imag % 1 == 0:
                        #print i, j, k,  self.trees[i], self.trees[j], self.trees[k],  center
                        triangles += 1
        return triangles
        
def main():
    """ Reads data from standard input, process, and write results to standard output """
    count = int(raw_input())
    for i in range(count):
        (n, A, B, C, D, x0, y0, M) = map(int, raw_input().split())
        f = CropField(n, A, B, C, D, x0, y0, M)
        #print f.trees
        print  'Case #' + str(i+1)  + ': ' + str(f.number_of_triangles())

main()
