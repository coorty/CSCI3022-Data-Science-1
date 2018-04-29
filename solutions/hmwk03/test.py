# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:26:01 2017
@author: zhaopace@foxmail.com
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.special import comb

#%%
def Poission(N):
    return np.exp(-20)*pow(20,N)/np.math.factorial(N)
prob_15=0
for N in range(0,16):
    prob_15+=Poission(N)
    
print('The probability that 15 boats or fewer cross under the bridge on a particular day =',prob_15)


#%%
def boat_time_sim(lam, num_boats=int(1e4)): 
    #20 boats per day
    #20/24 per hour
    beta = 1/(lam/24)
    two_hour_times=0
    two_boats_times=0
    time=0
    number=0
    for i in range(0,num_boats):
        time+=np.random.exponential(beta)
        #print(time,number)
        number+=1
        
        if time>2:
            if number==3:
                two_boats_times+=1
            
            two_hour_times+=1
            time-=2
            number=1
    
    print(two_boats_times/two_hour_times)

    
boat_time_sim(20)


#%%
def pmf_natural(x):
    if x>=1 and x<=9:
        return np.log10((x+1)/x)
    else:
        print('Input must be a number within 1 to 9')
        
# x的取值范围是1-9,对每个值进行概率计算
# Argu f(x) is a well-defined probability mass function
probs = []
for x in range(1,10):
    probs.append(pmf_natural(x))

print('Sum of the probability is: '+str(sum(probs)))

raiseTypeError



















