#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


ds=pd.read_csv("D:\president_heights.csv")


# In[5]:


ds


# In[6]:


ds.rename(columns={'height(cm)':'Height'})


# In[8]:


ds.rename(columns={'height(cm)':'Height'},inplace=True)


# In[9]:


ds


# In[10]:


ds.insert(3,"quality","good")


# In[11]:


ds


# In[13]:


ds.drop(columns=['quality'])


# In[14]:


ds


# In[16]:


ds.drop(columns=["quailty"],inplace=True)


# In[18]:


ds['Height']<175


# In[19]:


ds[ds['Height']>=175]


# In[23]:


ds[((ds['Height']>=175)&(ds['Height']<180))] 


# In[24]:


ds.isnull()


# In[25]:


ds


# In[31]:


sum(ds['Height'])


# In[32]:


import seaborn as sns


# In[39]:


mark=[99,99,99,99,99,99]
subject=['DBMS','PYTHON','JAVA','CLOUD','ML','MC']
plt.bar(subject,mark)
plt.xlabel("Subjects")
plt.ylabel("Mark")
plt.ylim(0,200)
plt.show()


# In[40]:


sns.barplot(x='name',y='Height',data=ds)


# In[ ]:




