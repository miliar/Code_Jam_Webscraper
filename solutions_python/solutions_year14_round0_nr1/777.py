#!/usr/bin/env pythom
#coding: utf-8

if __name__ == '__main__':
	fname = 'A-small-attempt0'
	with open('%s.in' % fname) as f, open('%s.out' % fname, 'w') as f2:
		n = int(f.readline())
		for case_i in xrange(n):
			first_answer = int(f.readline())
			first_matrix = []
			for line_i in xrange(4):
				first_matrix.append(f.readline().strip().split(' '))
			second_answer = int(f.readline())
			second_matrix = []
			for line_i in xrange(4):
				second_matrix.append(f.readline().strip().split(' '))
			result = []
			for check_i in xrange(4):
				if first_matrix[first_answer-1][check_i] in second_matrix[second_answer-1]:
					result.append(first_matrix[first_answer-1][check_i])
			if len(result) == 1:
				f2.write('Case #%s: %s\n' % (case_i+1, result[0]))
				# print result[0]
			elif len(result) > 1:
				f2.write('Case #%s: Bad magician!\n' % (case_i+1,))
				# print 'Bad magician!'
			elif len(result) == 0:
				f2.write('Case #%s: Volunteer cheated!\n' % (case_i+1,))
				# print 'Volunteer cheated!'


