#!/usr/bin/env python3
import subprocess
import sys
import os

# YOUR CODE GOES here


def tree(directory):
	dlist = sorted(os.listdir(directory))
	print(directory)
	numOfDir = 0
	numOfFile = 0
	stack = []
	for i in range(0, len(dlist)):
		if (i != len(dlist) - 1):
			prefix = '├── '
		else:
			prefix = '└── '
		stack.append((dlist[i], prefix, 0))
		discovered = []
		while (len(stack) != 0):
			d, prefix, indents = stack[-1]
			stack = stack[:-1]
			printD = d.split("/")[-1]
			print(indents * '│   ' + prefix + printD)
			if d not in discovered:
				discovered.append(d)
				newDir = os.path.join(directory, d)
				if os.path.isdir(newDir):
					numOfDir += 1
					sublist = sorted(os.listdir(newDir))
					for j in range(len(sublist) - 1, -1, -1):
						if (j != len(sublist) - 1):
							prefix = '├── '
						else:
							prefix = '└── '
						stack.append((d + "/" + sublist[j], prefix, indents + 1))
				else:
					numOfFile += 1
	print()
	print(str(numOfDir) + " directories, " + str(numOfFile) + " files")

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		tree(sys.argv[1])
	elif (len(sys.argv) == 1):
		tree('.')
	else:
		print("Please enter a directory!")
