# uses python3.6
# (potentially) uses additional libraries:
# numpy, scipy, sympy, networkx, matplotlib, sortedcontainers
# you can install them with 'pip3 install <library-name>'
import typing
from collections import defaultdict
from typing import List, Callable

import matplotlib, itertools
import scipy
import networkx as nx
from scipy.optimize import linprog
from sortedcontainers import sortedset, SortedSet

import constants
import datastructures
import graphs
import search
from d3 import collisions
from d3.vec3 import vec3
from datastructures.PriorityQueue import PriorityQueue
from datastructures.LinkedList import LinkedList
from ints.misc import odd, ncr_multinomial
from util import snd, fst, pairwise, ast_equals

matplotlib.use("TkAgg")
import numpy as np
from pprint import pprint as pp
import sys

from NumberGridPlotter import NumberGridPlotter
from d3.rectangle import rectangle
from d3.vec2 import vec2

import matplotlib.pyplot as plt
import queue, random, time, plotting
from d3.ipair import ipair, NESW4
import resource
from ints import primes

P_max = 10 ** 2
input_name = "B-small-practice"
input_name = "B-large-practice"
impossible = "IMPOSSIBLE"
input_name = "A-small-attempt0"
input_name = "test"
input_name = "A-large"


def solve(gets: Callable[[], List[str]], tid: int):
	nn, pp = map(int, gets())
	gg = list(map(int, gets()))
	gg = sorted(it % pp for it in gg)
	c0 = sum(it == 0 for it in gg)
	c1 = sum(it == 1 for it in gg)
	c2 = sum(it == 2 for it in gg)
	c3 = sum(it == 3 for it in gg)
	gg = [it for it in gg if it != 0]
	if pp == 2:
		res = c0 + (c1+1)//2
		return res
	elif pp == 3:
		res = c0
		res += min(c1, c2)
		tmp = max(c1,c2) - min(c1,c2)
		res += (tmp+2)//3
		return res
	else:
		res = c0
		res += min(c1, c3)
		tmp = max(c1, c3) - min(c1, c3)
		res += c2 // 2
		res += tmp // 4
		tmp%= 4
		c2 %=2
		if tmp + c2 > 0:
			res += 1
			if c2 ==1 and tmp >= 3:
				res += 1
		return res
	pass


# ==============================================
def solve_all_test_cases(T, lines):
	primes.make_primes_up_to(P_max)
	q = queue.Queue()
	for line in lines:
		q.put(line.split())
	
	def q_get():
		return q.get()
	
	for test_case_id in range(1, T + 1):
		result = solve(q_get, test_case_id)
		if type(result) in {float, np.float32, np.float64}:
			result = f"{result:.8f}"
		text = "Case #{}: {}".format(test_case_id, result)
		write(text)


res_path = "../../../../downloads/"
output_path = res_path + input_name + ".out"
last_output = None
import os

if os.path.isfile(output_path):
	last_output = "".join(open(output_path).readlines())
current_output = ""
output = open(output_path, "w")


def mymain():
	input_lines = open(res_path + input_name + ".in").readlines()
	input_lines = [line.strip() for line in input_lines]
	T = int(input_lines[0])
	input_lines = input_lines[1:]
	solve_all_test_cases(T, input_lines)


def write(text):
	if text[-1] != "\n":
		text += "\n"
	print(text, end="", flush=True)
	global current_output
	current_output += text
	output.write(text)


if __name__ == "__main__":
	max_heap_size = 10 ** 9
	resource.setrlimit(resource.RLIMIT_DATA, (max_heap_size, max_heap_size))
	print(f"solving input file: {input_name}.in")
	start = time.time()
	random.seed(0)
	np.random.seed(0)
	sys.setrecursionlimit(2500)
	mymain()
	end = time.time()
	s = end - start
	m = int(s / 60)
	print("=" * 20)
	print(f"elapsed time: {s:.2f}s = {m}m {round(s)%60}s")
	print(f"results written to: {output_path}")
	if current_output == last_output:
		print("*****SAME*****")
	else:
		print("=====CHANGED=====")
