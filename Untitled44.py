#!/usr/bin/env python
# coding: utf-8

# In[10]:


list = [8, 2, 3, 0, 7]
def sumOfList(List, size):
    if(size == 0):
        return 0
    else:
         return list[size - 1] + sumOfList(list, size-1)
   
    total = sumOfList(list, len(list))
print("sumOfList: ",total)    


# In[ ]:




