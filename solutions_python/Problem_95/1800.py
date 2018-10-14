#!/usr/bin/env python2.7
# -*- coding: utf8 -*-


with open('A-small-attempt0.in', 'r') as f, open('A-small.out', 'w') as out, open('learn', 'r') as flearn:

    l = flearn.readlines()
    from_ = l[0:3]
    to = l[3:]

    translation_map = dict()

    for sindex, sentense in enumerate(from_):
        for cindex, c in enumerate(sentense):
            if not c in translation_map and c.strip():
                translation_map.update({c:to[sindex][cindex]})

    translation_map.update({'z':'q', 'q':'z'})

    count = int(f.readline())

    for line_index, line in enumerate(f):

        line_out = ''
        for c in line:
            if c.strip():
                line_out = ''.join([line_out, translation_map[c]])
            else:
                line_out = ''.join([line_out, c])


        #print 'Case #%d: %s' % (line_index+1, line_out.strip())
        out.write('Case #%d: %s' % (line_index+1, line_out))



