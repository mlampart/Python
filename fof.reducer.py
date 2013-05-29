#!/usr/bin/env python
import sys
import itertools

previd=-1
prev1=-1
prev2=-1
out=0;

for line in sys.stdin:
	triplet = line.split()
	if triplet[0] == previd and triplet[1] == prev1 and triplet[2] == prev2:
		if out == 0:
			print triplet
			out = 1
	else:
		out = 0
		previd = triplet[0]
		prev1 = triplet[1]
		prev2 = triplet[2]
