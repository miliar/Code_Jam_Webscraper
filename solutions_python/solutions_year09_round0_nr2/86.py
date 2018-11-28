#!/usr/bin/env python

graph = [];
mark = [];
direction = [[-1, 0], [0, -1], [0, 1], [1, 0]];
ch = 'a';
numX = 0;
numY = 0;

def findSink(x, y):
#    if mark[x][y] == '\0':
#        break;
    global ch, graph, mark, direction, numX, numY;
    minHeight = graph[x][y];
    for i in range(4):
        if x + direction[i][0] >= 0 and x + direction[i][0] < numX \
           and y + direction[i][1] >= 0 and y + direction[i][1] < numY:
           if graph[x + direction[i][0]][y + direction[i][1]] < minHeight:
               xx = x + direction[i][0];
               yy = y + direction[i][1];
               minHeight = graph[xx][yy];
    if minHeight != graph[x][y]:
        if mark[xx][yy] == '\0':
            mark[x][y] = findSink(xx, yy);
        else:
            mark[x][y] = mark[xx][yy];
    else:
        mark[x][y] = ch;
        ch = chr(ord(ch)+1);
    return mark[x][y];

def main():
    global ch, graph, mark, direction, numX, numY;
    fin = open("B-large.in","r");
    fout = open("output.out","w");
    n = int(fin.readline());
    str = [];

    for i in range(n):
        str = (fin.readline().split());
        numX = int(str[0]);
        numY = int(str[1]);
        for x in range(numX):
            graph.append([]);
            mark.append([]);
            str = fin.readline().split();
            for y in range(numY):
                graph[x].append(int(str[y]));
                mark[x].append('\0');
#        for x in range(numX):
#            for y in range(numY):
#                print('{0} '.format(graph[x][y]));          
        for x in range(numX):
            for y in range(numY):
                if mark[x][y] == '\0':
                    findSink(x,y);
        fout.write("Case #{0}:\n".format(i+1));
        for x in range(numX):
            for y in range(numY):
                if y != numY - 1:
                    fout.write("{0} ".format(mark[x][y]));
                else:
                    fout.write("{0}\n".format(mark[x][y]));
        graph = [];
        mark = [];
        ch = 'a';
#        print n;
#        print strX,strY;

if __name__ == '__main__':
    main();
