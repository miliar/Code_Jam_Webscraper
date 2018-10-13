#!/usr/bin/env python

#
# Google Code Jam 2012
# Nathan Williams <nlwsother@gmail.com>
#

import sys
import string

def add_mapping(mapdict, goog_text, eng_text):
    i = 0
    while i < len(goog_text):
        g = goog_text[i]
        e = eng_text[i]
        if g in mapdict:
            cure = mapdict[g]
            if cure != e:
                print "Mapping discrepancy: goog='%s' old='%s' new='%s'" % (g, cure, e)
        else:
            mapdict[g] = e
        i = i + 1

def goog_to_eng(mapdict, goog_text):
    out_text = ''
    for g in goog_text:
        if g in mapdict:
            out_text = out_text + mapdict[g]
        else:
            out_text = out_text + '?'
    return out_text

def fill_in_missing(mapdict):
    used_e = []
    used_g = []
    unused_e = [' ']
    unused_g = [' ']
    for s in string.ascii_lowercase:
        unused_e.append(s)
        unused_g.append(s)
    for g,e in mapdict.iteritems():
        unused_e.remove(e)
        unused_g.remove(g)
        used_e.append(e)
        used_g.append(g)

    len_e = len(unused_e)
    len_g = len(unused_g)
    if len_e == len_g == 0:
        print "No remaining mappings"
    elif len_e != len_g or len_e > 1:
        print "Too many remaining unused: e='%s' g='%s'" % (unused_e, unused_g)
    else:
        g = unused_g[0]
        e = unused_e[0]
        #print "Adding mapping: '%s'='%s'" % (g, e)
        mapdict[g] = e


mapping = {}

# Initial mappings, from problem example
add_mapping(mapping, ' ', ' ')
add_mapping(mapping, 'y qee', 'a zoo')
add_mapping(mapping, 'ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
add_mapping(mapping, 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
add_mapping(mapping, 'de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')

fill_in_missing(mapping)

#if len(mapping) != (len(string.ascii_lowercase) + 1):
#    print "Not a complete mapping", len(mapping), mapping
#else:
#    print "Complete goog_to_eng:", goog_to_eng(mapping, string.ascii_lowercase)


if len(sys.argv) == 1:
    sys.exit(0)

if len(sys.argv) > 2:
    print "Too many command line arguments"


#print "Processing", sys.argv[1], "\n\n"

read_count = False
read_lines = 0
input_file = open(sys.argv[1])

for cur_line in input_file:
    if read_count is False:
        read_count = int(cur_line)
    elif read_lines == read_count:
        break
    else:
        read_lines += 1
        # Spec: no spaces at begin or end of line
        goog_text = cur_line.strip()
        eng_text = goog_to_eng(mapping, goog_text)
        print 'Case #%d: %s' % (read_lines, eng_text)

