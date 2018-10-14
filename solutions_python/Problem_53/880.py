#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def light_state(num_of_snapper,snap_times):
	'''num_of_snapper個のSnapperをつないでsnap_times回音をならした時のライトの状態

	>>> light_state(1,0)
	'OFF'
	>>> light_state(1,1)
	'ON'
	>>> light_state(4,0)
	'OFF'
	>>> light_state(4,47)
	'ON'
	'''
	# 音を鳴らした回数を２進数表記すると、0,1がスイッチのOFF,ONに対応する
	binary = int2binary(snap_times)[-num_of_snapper:]

	# ライトまで来てない場合
	if len(binary) < num_of_snapper: return 'OFF'

	# すべて1だったらライトがつく
	if binary == '1' * num_of_snapper: return 'ON'
	return 'OFF'

def int2binary(integer):
	'''整数から２進数文字列へ変換

	>>> int2binary(2)
	'10'
	>>> int2binary(4)
	'100'
	>>> int2binary(11)
	'1011'
	'''
	octal = '%o'%integer
	binary = ''
	octal2binary = {
			'0':'000',
			'1':'001',
			'2':'010',
			'3':'011',
			'4':'100',
			'5':'101',
			'6':'110',
			'7':'111',
			}
	for o in octal:
		binary += octal2binary[o]
	return binary.lstrip('0')

def main():
	count = int(sys.stdin.readline())
	for i in xrange(1,count+1):
		line = sys.stdin.readline()
		(num_of_snapper,snap_times)=line.split()
		print 'Case #'+str(i)+': '+light_state(int(num_of_snapper),int(snap_times))

def test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	main()

