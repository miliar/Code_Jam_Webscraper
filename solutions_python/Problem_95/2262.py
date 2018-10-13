#!/usr/bin/env python 
######################################################################
## Filename:    A.py
## Version:     $Revision: 1.0 $
## Description: 
## Creator:     Rui Pereira <rui.pereira@in2p3.fr>
## Created:     14-04-2012 18:06:30
## Modified:    Time-stamp: <2012-04-14 18:21:42 rui>
## CVS info:    $Id: A.py, v 1.0 14-04-2012 18:06:30 pereira Exp $
######################################################################
"""
"""

__author__ = 'Rui Pereira <rui.pereira@in2p3.fr>'
__version__ = '$Revision$'

import sys

inputs = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv']
outputs = ['our language is impossible to understand',
           'there are twenty six factorial possibilities',
           'so it is okay if you want to just give up']

t = {}
for i,o in zip(inputs, outputs):
    t.update({a:b for a,b in zip(i,o)})

t.update({'q':'z', 'z':'q'})
translate = lambda s: ''.join([t[i] for i in s])

for n,l in enumerate(open(sys.argv[1]).read().splitlines()[1:]):
    print 'Case #%i: %s' % (n+1, translate(l.strip()))
