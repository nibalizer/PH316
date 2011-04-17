#!/usr/bin/python2.6

import numpy as np
import pylab as plt
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
f.closed
tline = lines
lines = [line.rstrip() for line in tline]


#for line in lines:
#    print "{0}\t{1}".format(lines.index(line), line)

better = lines[13:]

#for line in better:
#    print "{0}\t{1}".format(better.index(line), line)
    

def chopchop(elements, unitsize):
    chunks = []
    for i in range(0, len(elements)-1, unitsize):
        chunks.append(elements[i:i+unitsize])
    return chunks



chunks = chopchop(better, 24)

#print chunks[-1]
low= chunks[0][2]
high= chunks[-1][2]


for chunk in chunks:
    vals = chunk[4:]
    xs, ys = [], []
    for val in vals:
        x,y = map(float, val.split(','))
        xs.append(x)
        ys.append(y)
    plt.plot(xs,ys, 'o')
        
plt.title("{0}-{1} angstroms".format(low, high))
plt.show()



