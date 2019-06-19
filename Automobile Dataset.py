#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #this will import pandas into your workspace


# In[2]:


import numpy as np  #we will be using numpy functions so import numpy


# In[3]:


cars = pd.read_csv('cars.csv')#(your_local_path+'cars.csv')


# In[4]:


type(cars)
cars.head(20)


# In[5]:


carsgrp = cars.groupby('Cylinders').mean()     # Data GROUP BY
carsgrp2 = cars.groupby('Cylinders')
carsgrp
#round(carsgrp,2)


# In[8]:


# Pivot table demo
table = pd.pivot_table(cars, values='Actual_MPG', index=['Cylinders','Origin'],columns=['Weight','Year'], aggfunc=np.median)
table2 = pd.pivot_table(cars, values=('Actual_MPG','Horsepower'), index=['Origin', 'Cylinders'],columns=['Year'])
#round(table,2)
#print (table)
table2


# In[7]:


import matplotlib.pyplot as plt
import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


#scatter plots
# first let's create a x variable
plt.scatter(cars.Weight,cars.Actual_MPG,color ='purple')
#plt.plot(cars.Actual_MPG,color ='purple')
plt.xlabel ('Weight')
plt.ylabel ('Actual_MPG')
plt.show()


# In[10]:


#scatter plots
plt.plot(carsgrp.Horsepower,carsgrp.Actual_MPG,'b',linestyle = '--',color ='red', linewidth = 4.5)
#plt.plot(carsgrp.Horsepower,carsgrp.Actual_MPG)
plt.xlabel ('Horsepower')
plt.ylabel ('Actual_MPG')
plt.title ('Horsepower vs MPG Trend')
plt.show()


# In[11]:


#left # the left side of the subplots of the figure
#right # the right side of the subplots of the figure
#bottom # the bottom of the subplots of the figure
#top # the top of the subplots of the figure
#wspace # the amount of width reserved for blank space between subplots
#hspace # the amount of height reserved for white space between subplots'''
plt.figure(figsize=(20,10))
plt.subplots_adjust(hspace= 0.2, wspace= 0.2)
plt.subplot(2,2,1)
plt.title ('Actual_MPG')
plt.plot(cars.Actual_MPG,'r')
plt.subplot(2,2,2)
plt.title ('Weight')
plt.plot(cars.Weight, 'b')
plt.subplot(2,2,3)
plt.title ('Cylinders')
plt.plot(cars.Cylinders, 'g')
plt.subplot(2,2,4)
plt.title ('Horsepower')
plt.plot(cars.Horsepower,'y')
plt.show()


# In[12]:


plt.figure(figsize=(15,5))
plt.subplots_adjust( wspace= 0.5)
plt.subplot(1,4,1)
plt.title ('Actual_MPG')
plt.plot(cars.Actual_MPG,'r')
plt.subplot(1,4,2)
plt.title ('Weight')
plt.plot(cars.Weight, 'b')
plt.subplot(1,4,3)
plt.title ('Cylinders')
plt.plot(cars.Cylinders, 'g')
plt.subplot(1,4,4)
plt.title ('Horsepower')
plt.plot(cars.Horsepower,'y')


# In[ ]:




