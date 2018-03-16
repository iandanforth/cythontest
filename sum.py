from __future__ import division
from random import randint
from csum import csum
from time import time

def pysum(vals):

    total = 0
    for v in vals:
        total += v

    return total


def main():
    vals = [randint(1, 100) for _ in xrange(1000000)]

    start = time()
    print csum(vals)
    cdur = time() - start
    print 'Cython', cdur

    start = time()
    print pysum(vals)
    pydur = time() - start
    print 'Python', pydur

    print 'Speedup', pydur / cdur

if __name__ == '__main__':
    main()
