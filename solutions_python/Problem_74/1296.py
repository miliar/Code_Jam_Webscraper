#!/usr/local/bin/python2.6
import codejam
import problemA
import sys

options, args = codejam.get_simple_options( sys.argv, { 'debug_level': 0, 'problem': 'A', 'size': 'small', 'number': 0 } )
prefix = '%s-%s-%s' % (options.problem, options.size, options.number)

print("Running on input prefix '%s'..." % prefix)

codejam.run_cases( prefix, problemA.runner, int(options.debug_level) )
codejam.pause()
