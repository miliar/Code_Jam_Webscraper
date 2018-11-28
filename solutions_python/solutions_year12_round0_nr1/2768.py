#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import string

intab = 'ynficwlbkuomxsevzpdrjgthaq'
outtab =  'abcdefghijklmnopqrstuvwxyz'
trantab = string.maketrans(intab, outtab)

cases = raw_input()
for case in range(1, int(cases)+1):
	crypt = raw_input()
	print 'Case #%s: %s' % (case, crypt.translate(trantab))
