__author__ = 'Christian'

#fname = 'test_b.txt'
fname = 'B-small-attempt1.in'
#fname = 'B-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')



T = int(data[0])
for i in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in data[i+1].split(' ')]

    l = [[R, 'R'], [B, 'B'], [Y,'Y']]
    l.sort(reverse=True)
    main_col = l[0]
    second_col = l[1]
    third_col = l[2]

    if main_col[0] > second_col[0] + third_col[0]:
        print >> res_file, "Case #%s: IMPOSSIBLE" % (i + 1)
    else:
        n = (main_col[0]-third_col[0])
        res = (main_col[1] + second_col[1]) * n
        main_col[0] = third_col[0]
        second_col[0] = second_col[0] - n
        res += (main_col[1] + second_col[1] + third_col[1]) * second_col[0]
        main_col[0] = main_col[0] - second_col[0]
        res += (main_col[1]+third_col[1]) * main_col[0]
        print >> res_file, "Case #%s: %s" % (i+1, res)
    
res_file.close()