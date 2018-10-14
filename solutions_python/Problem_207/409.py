from timeit import default_timer as timer

def horses(n, r, o, y, g, b, v):
        if r < g or b < o or y < v or r+b+v < y or r+y+o < b or y+b+g < r:
                return 'IMPOSSIBLE'
        else:
                arrange = ''
                colors = [r, o, y, g, b, v]
                color_str = 'ROYGBV'
                neighbours = ['YBG', 'B', 'RBV', 'R', 'RYO', 'Y']
                for i in xrange(n):
                        if i == 0:
                                j = 0
                                while colors[j] == 0:
                                        j += 1
                                colors[j] -= 1        
                                arrange = color_str[j]
                        else:
                                #print arrange, colors
                                max_col = 0
                                col = ''
                                for s in neighbours[color_str.index(arrange[-1])]:
                                        if s in 'OGV' and colors[color_str.index(s)] > 0:
                                                max_col = 1000
                                                col = s
                                        elif colors[color_str.index(s)] > max_col:
                                                max_col = colors[color_str.index(s)]
                                                col = s
                                if col == '':
                                        return 'CHECKYOWORK'
                                else:
                                        arrange += col
                                        colors[color_str.index(col)] -= 1

                return arrange
        
	
start = timer()
filename = 'B-small-attempt0'
f_in = open(filename + '.in', 'r')
f_out = open(filename + '.out', 'w')
t = int(f_in.readline())

for i in xrange(1, t+1):
	n, r, o, y, g, b, v = [int(x) for x in f_in.readline().split(' ')]
	f_out.write('Case #' + str(i) + ': ' + horses(n, r, o, y, g, b, v) + '\n')

f_in.close()
f_out.close()
end = timer()
print (end - start)
