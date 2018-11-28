'''
Created on Sep 3, 2009
@author: namnx
'''
import string
INFILE = 'watersheds-large.in'
OUTFILE = 'watersheds-large.out'


def next(x,y,a):
    h = len(a)
    w = len(a[0])
    result = [x,y]
    if (x>0) and (a[result[0]][result[1]] > a[x-1][y]):
        result = (x-1,y)
    if (y>0) and (a[result[0]][result[1]] > a[x][y-1]):
        result = (x,y-1)
    if (y<w-1) and (a[result[0]][result[1]] > a[x][y+1]):
        result = (x, y+1)
    if (x<h-1) and (a[result[0]][result[1]] > a[x+1][y]):
        result = (x+1, y)
    if result == [x,y]:
        return None
    return result


def findLabel(x,y,a,labels):
    while(labels[x][y] == '0' and next(x,y,a) != None):
        (x,y) = next(x,y,a)
    return labels[x][y]


def applyLabels(x,y,a,labels,label):
    labels[x][y]=label
    while(next(x,y,a) != None):
        (x,y) = next(x,y,a)
        labels[x][y] = label


def solve(a):
    labels = []
    for i in range(len(a)):
        labels.append([])
        for j in range(len(a[0])):
            labels[i].append('0')
    
    currentLabel = 'a'
    for i in range(len(a)):
        for j in range(len(a[0])):
            if (labels[i][j] == '0'):
                label = findLabel(i,j,a, labels)
                if label != '0':
                    applyLabels(i, j, a, labels, label)
                else:
                    applyLabels(i, j, a, labels, currentLabel)
                    currentLabel = chr(ord(currentLabel)+1)
    return labels


def main():
    fin = file(INFILE, 'r')
    fout = file(OUTFILE, 'w')
    t = int(fin.readline())
    for i in range(t):
        dimension = fin.readline().strip().split()
        height = int(dimension[0])
        width = int(dimension[1])
        a = []
        for j in range(height):
            a.append([])
            line = fin.readline().strip().split()
            for k in range(width):
                a[j].append(int(line[k]))
        result = solve(a)
        fout.write('Case #' + str(i+1) + ':\n')
        for line in result:
            for c in line:
                fout.write(c + ' ')
            fout.write('\n')
    fin.close()
    fout.close()
    return


if __name__ == '__main__':
    main()