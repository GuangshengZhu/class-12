
import numpy as np

def getBondPrice(y,face,couponRate,m,ppy=1):
    y = y / ppy
    c = couponRate / ppy
    m = m * ppy
    p=1+y
    d1=[p]
    d1=d1*m
    d1=np.array(d1)
    d2=np.arange(1,m+1)*-1
    d3=d1**d2
    price=(sum(d3)*c+d3[m-1])*face
    return(price)


y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy=2

getBondPrice(y,face,couponRate,m,ppy)
