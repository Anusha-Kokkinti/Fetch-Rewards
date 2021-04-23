#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv(r'C:\Users\HP\Desktop\test\p\brands.csv')


# In[5]:


df.head()


# In[26]:


data_types = pd.DataFrame(
    df.dtypes,
    columns=['Data Type'])


# In[27]:


#Checking the datatypes
data_types


# In[16]:


#Renaming the columns
df.columns = ['BrandID', 'barcode', 'category', 'categorycode', 'cpgid','cpgref','name','topbrand','brandcode']


# In[17]:


df


# In[18]:


missing_data = pd.DataFrame(
    df.isnull().sum(),
    columns=['Missing Values'])


# In[19]:


# checking for missing data
missing_data


# In[20]:


unique_values = pd.DataFrame(columns=['Unique Values'])
for row in list(df.columns.values):
    unique_values.loc[row] = [df[row].nunique()]


# In[21]:


#Checking for Unique values
unique_values


# In[22]:


df.info()


# In[28]:


dq_report = data_types.join(missing_data).join(unique_values)
dq_report


# In[ ]:




