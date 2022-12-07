
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    y = y / ppy
    c = couponRate / ppy
    m = m * ppy
    p = 1 + y
    d1 = [p]
    d1 = d1 * m
    d1 = np.array(d1)
    d2 = np.arange(1, m + 1) * -1
    d3 = d1 ** d2
    cf=c*face
    l1=[cf]*(m-1)
    l1.append(cf+face)
    l1=np.array(l1)
    l2=l1*d3
    d4=d2*-1
    duration=sum(d4*l2)/sum(l2)
    return(duration)

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

getBondDuration(y,face,couponRate,m,ppy)
