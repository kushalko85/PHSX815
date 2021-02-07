#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Read file and save in array, code suppose there is a file containing random number
    rnd = []
    rnd = np.loadtxt("random.txt")
    print(rnd)

    # create histogram of our data
    n, bins, patches = plt.hist(rnd ,50, density=True, facecolor='green', histtype ="stepfilled", alpha=0.45)

    # plot formating options
    plt.xlabel('x')
    plt.ylabel('Probability Density' , fontweight="bold" , fontsize="17")
    plt.title('Uniform random number' , fontweight="bold" , fontname="sans serif")
    plt.grid(True , color='r')

    # show figure (program only ends once closed
    plt.show()


# In[ ]:




