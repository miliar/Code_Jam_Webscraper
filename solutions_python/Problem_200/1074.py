from timeit import default_timer as timer

def last_tidy(n_str):
#        print n_str
        if tidy(n_str):
                return n_str
        else:
                x_str = last_tidy(n_str[1:])
                if x_str[0] >= n_str[0]:
#                        print 'Returned[1]: ' + n_str[0] + x_str
                        return n_str[0] + x_str
                else:
#                        print 'Returned[2]: ' + str(int(n_str[0])-1) + '9'*len(x_str)
                        return str(int(n_str[0])-1) + '9'*(len(n_str) - 1)

def tidy(n_str):
        x = [int(n_str[i]) <= int(n_str[i+1]) for i in xrange(len(n_str)-1)]
        return x == [True]*(len(n_str) - 1)

start = timer()
filename = 'B-large'
f = open(filename + '.in', 'r')
g = open(filename + '.out', 'w')
t = int(f.readline())

for i in xrange(1, t+1):
	n = int(f.readline())
	g.write('Case #' + str(i) + ': ' + str(int(last_tidy(str(n)))) + '\n')

f.close()
g.close()
end = timer()
print (end - start)
