#!/usr/bin/env python
import sys
import itertools

for line in sys.stdin:
	#line = line.strip()
	#ID,friends = line.split(' ',1)	
	friends = line.split()
	ID = friends[0]
	size = len(friends)
	for f in xrange(1,size):
		for g in xrange(f+1,size):
			if ID<friends[g]:
				print friends[f],ID,friends[g]
			else:
				print friends[f],friends[g],ID
			if ID<friends[f]:
				print friends[g],ID,friends[f]
			else:
				print friends[g],friends[f],ID
