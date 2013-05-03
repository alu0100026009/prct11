#! /usr/bin/python

import sys
import timeit
from math import *

if __name__ == '__main__':
  
  expr1 = (sys.argv[1])
  expr2 = (sys.argv[2])
  
  t1 = timeit.Timer(expr1, setup='import random; a = random.uniform(0,100); b = random.uniform(0,100)')
  t2 = timeit.Timer(expr2, setup='import random; a = random.uniform(0,100); b = random.uniform(0,100)')
  t11=t1.timeit(10000000)
  t12=t2.timeit(10000000)

  if t11 < t12:
    print ('La expresion %s es un %f %s mas rapida que la expresion %s' %(expr1,100-(t1.timeit(10000000)*100/t2.timeit(10000000)),'%',expr2))
  else:
    print ('La expresion %s es un %f %s mas rapida que la expresion %s' %(expr2,100-(t2.timeit(10000000)*100/t1.timeit(10000000)),'%',expr1))