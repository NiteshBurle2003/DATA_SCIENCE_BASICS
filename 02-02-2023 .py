#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(a)


# In[17]:


b=a


# In[18]:


print(b)


# In[19]:


print(a)


# In[20]:


c=np.array([[4,3,2,1],[8,7,6,5],[12,11,10,9],[16,15,14,13]])
print(c)


# In[ ]:





# In[21]:


c.T


# In[22]:


c[:,1]


# In[23]:


b+c


# In[24]:


np.add(b,c)


# In[25]:


np.subtract(b,c)


# In[26]:


b-c


# In[27]:


b*c


# In[29]:


np.multiply(b,c)


# In[30]:


np.divide(b,c)


# In[31]:


b/c


# In[32]:


np.sqrt(b)


# In[33]:


import matplotlib.pyplot as plt


# In[34]:


x=np.arange(0,5,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()


# In[52]:


o=[1,2,3,4,5,6,7,8,9,10]
Ind=[10,8,11,5,9,9,14,11,13,17]
Aus=[9,5,2,0,5,14,10,12,12,9]
plt.plot(o,Ind)
plt.plot(o,Aus)
plt.legend(o)
plt.title("Match Overall Run Rate")
plt.xlabel("No.of Overs")
plt.ylabel("RunRate")
plt.show()


# In[46]:


import pandas as pd


# In[55]:


ds=pd.read_csv("D:\president_heights.csv")


# In[56]:


ds


# In[58]:


ds.info()


# In[59]:


ds.dtypes


# In[61]:


ds1=ds


# In[62]:


ds


# In[67]:


ds1.head(10)


# In[66]:


ds.tail()


# In[68]:


ds.head(1)


# In[69]:


ds.iloc[35]


# In[73]:


ds.iloc[35:39]


# In[74]:


ds1.describe()


# In[81]:


ds1['order'].describe()


# In[82]:


subset=ds1[['order','name']]


# In[84]:


subset


# In[85]:


del subset['order']


# In[86]:


subset


# In[87]:


ds1.rename(columns={'order':'ordernumber'})


# In[88]:


ds1.columns


# In[89]:


ds1


# In[91]:


ds1.insert(7,"8","Dr.Nihanth the Emperor","176")


# In[93]:


ds1=ds
ds1.iloc[4]


# In[94]:


ds1.iloc[4]=5,"Nihanth","176"


# In[95]:


ds1.iloc[4]


# In[99]:


del ds1["order"]


# In[100]:


ds1


# In[ ]:




