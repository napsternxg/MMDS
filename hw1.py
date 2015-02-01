# coding: utf-8

import numpy as np

# Function for checking number is prime
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0:
        return False
    if n < 2:
        return False
    for i in range(5,int(n**0.5),2):
        if n % i == 0:
            return False
    return True

# Mapper function
def map(i):
    if i < 2:
        return []
    pDivs = []
    if i % 2 == 0:
        pDivs.append((2,i))
    for n in range(3,int(i**0.5)+1,2):
        if isPrime(n) and (i % n == 0):
            pDivs.append((n,i))
            if (i/n != n) and isPrime(i/n):
                pDivs.append((i/n,i))
    return pDivs
#reducer function
def reduce(p,iArr):
    return p,sum(iArr)

def groupBy(pDivsArr):
    pDict= {}
    for pDivs in pDivsArr:
        for p,v in pDivs:
            if p not in pDict:
                pDict[p] = []
            pDict[p].append(v)
    return pDict
pDivsArr = [map(k) for k in [15, 21, 24, 30, 49]]
[reduce(p,v) for p,v in groupBy(pDivsArr).iteritems()]
print pDivsArr

# Solution for Question 1-3

# Question 1
a = np.array([[0, 0.5, 0.5],[0,0,1],[0,0,1]])
m = a
b = 0.7
m = m.T
a = b*m + ((1-b)/3)*e.T.dot(e)
eg,ev  = np.linalg.eig(a)
r  = np.ones([3,1])
r0 = r
for i in range(5):
  r = a.dot(r)
  print r
r[0]
r[0]+r[1]
r[2]+r[1]
r[2]+r[0]

# Question 2
m = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
b = 0.85
a = b*m + ((1-b)/3)*e.T.dot(e)
r = np.ones([3,1])
for i in range(5):
  r = a.dot(r)
  print r
np.linalg.eig(a)
eg,ev = np.linalg.eig(a)

# Question 3 (it has same network structure as question 2 so using same m)
r = np.ones([3,1])
r_arr = [r]
r_arr
for i in range(1,6):
    r_arr[i] = m.dot(r_arr[i-1])
    
r_arr[i]
for i in range(1,6):
    r_arr.append(m.dot(r_arr[i-1]))
r_arr[4]
