{\rtf1\ansi\ansicpg1252\cocoartf949\cocoasubrtf540
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww9000\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\ql\qnatural\pardirnatural

\f0\fs24 \cf0 def get_rows(lines):\
	if lines == 1:\
		return map(float, raw_input().split())\
	return [map(float, raw_input().split()) for _ in range(lines)]\
\
def drange(start, stop, step):\
	r = start\
	while r < stop:\
		yield r\
		r += step\
\
def get_result(row):\
	C, F, X = row\
	mult = 2\
	best = X / mult\
	while 1:\
		next_sum = sum(float(C) / i for i in drange(2, mult + F, F)) + X / (mult + F)\
		if next_sum > best:\
			return best\
		best = next_sum\
		mult += F\
		\
cases = input()\
\
for i in range(1, cases + 1):\
	row = get_rows(1)\
	result = get_result(row)\
	print "Case #\{0\}: \{1\}".format(i, result)\
}