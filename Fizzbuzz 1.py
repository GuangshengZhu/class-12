
import numpy as np

def FizzBuzz(start, finish):
    finish+=1
    numvec = np.arange(start, finish)
    objvec = np.array(numvec, dtype=object)
    d1= (objvec%3==0) & (objvec%5 !=0)
    d2= (objvec%5==0) & (objvec%3 !=0)
    d3= objvec%15==0
    objvec[d1] = 'fizz'
    objvec[d2] = 'buzz'
    objvec[d3] = 'fizzbuzz'
    return(objvec)

start = 46
finish = 60

FizzBuzz(start,finish)