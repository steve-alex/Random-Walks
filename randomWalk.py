import numpy as np
from numpy import diff, log, exp, cumsum 
import matplotlib.pyplot as plt
import random
# http://sphelps.net/teaching/scf/slides/random-walks-slides.html#/0/2

def randomWalk(steps, prob):
    '''Computes a randomWalk with number of steps and probabilty of up
    movement inputed by the user.
    Function plots the random walk and prints minimum and maximum values.'''

    position = 0
    walk = [position]
    
    for i in range(steps):
        if np.random.binomial(1, prob) == 1:
            step = 1
        else:
            step = -1
            
        position += step
        walk.append(position)
        
    plt.plot(walk[:])
    print('Maximum value is', walk.max())
    print('Minimum value is', walk.min())


def nRandomWalks(n, steps, prob):
    '''
    n: number of 'paths'
    Steps: number of movements
    Prob: Probability of up movements
    '''
    
    numbers = np.randint(0, 2, size=(steps, n))
    movements = np.where(numbers == 0, 1, -1)
    values = np.cumsum(movements, axis=0)
    plt.xlabel('Time')
    plt.ylalbel('Y')
    ax = plt.plot(values)


def multiplicativeRandomWalk():
    initial_value = 100.0
    random_numbers = np.random.normal(size=steps) * 0.005
    multipliers = 1 + random_numbers
    values = initial_value * np.cumprod(multipliers)
    plt.xlabel('t')
    plt.ylabel('y')
    ax = plt.plot(values)
    plt.xlabel('t')
    plt.ylabel('r')
    ex = plt.plot(random_numbers)


def multiplicativeLogRandomWalks():
    t_max = 100
    volatility = 1.0/100.0
    initial_value = 100.0
    r = normal(size=t_max)*volatility
    y = initial_value * exp(cumsum(r))
    plt.xlabel('t')
    plt.ylabel('y')
    ax = plt.plot(y)


def nMultiplicativeLogRandomWalks(initial_value=100, n=10,
                                  t_max=100, volatility = 0.005):
    r = np.random.normal(size=(t_max+1, n)*volatility)
    return initial_value * exp(np.cumsum(r, axis=0))

    plt.xlabel('t')
    plt.ylabel('y')
    ax = plt.plot(nMultiplicativeLogRandomWalks(n=10))    
