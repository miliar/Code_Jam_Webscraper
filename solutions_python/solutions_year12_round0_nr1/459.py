#!/usr/bin/env python
# coding: utf-8

import sys

with open('sample.in') as infile, open('sample.out') as outfile:
    inlines = [line.strip() for line in infile][1:];
    outlines = [line.strip().split(": ")[1] for line in outfile];
    outstr = "";
    for outline in outlines:
        for outwd in outline.split():
            outstr += outwd;
    instr = "";
    for inline in inlines:
        for inwd in inline.split():
            instr += inwd;
    gmap = dict();
    for i in range(len(instr)):
        gmap[instr[i]] = outstr[i];

with open(sys.argv[1]) as infile:
    inlines = [line.strip() for line in infile][1:];
    gmap['z'] = 'q';
    gmap['q'] = 'z';
    gmap[' '] = ' ';
    cid = 0;
    for line in inlines:
        cid += 1;
        outline = "";
        for c in line:
            outline += gmap[c];
        print "Case #%d: %s" % (cid, outline);
