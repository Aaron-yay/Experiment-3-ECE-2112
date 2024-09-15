#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[97]:


C = pd.read_csv('cars.csv')


# In[99]:


C


# In[25]:


B = C.head()


# In[27]:


B


# In[89]:


#a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
B.iloc[:, 0:12:2] 


# In[139]:


#b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
B.loc[B['Model'] == 'Mazda RX4']


# In[141]:


#c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
C.loc[C['Model'] == 'Camaro Z28', ['cyl']]


# In[165]:


#Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
C.loc[(C['Model']=='Mazda RX4 Wag')|(C['Model']=='Ford Pantera L')|(C['Model']=='Honda Civic'),['cyl','gear']]


# In[ ]:




