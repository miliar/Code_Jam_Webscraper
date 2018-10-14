# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python
import sys
import random
import numpy as np
from time import time
import math

T = int(raw_input().strip())
for n in range(T):
	D, N = map(int, raw_input().strip().split(' '))
	lastTime = -1
	for i in range(N):
		start, speed = map(int, raw_input().strip().split(' '))
		if lastTime < 0:
			lastTime = (D - start * 1.0)/speed
		else:
			lastTime = max(lastTime, (D - start * 1.0)/speed)
	MaxSpeed = (1.0)*D/lastTime
	print("Case #"+str(n+1) + ": "+str(MaxSpeed))