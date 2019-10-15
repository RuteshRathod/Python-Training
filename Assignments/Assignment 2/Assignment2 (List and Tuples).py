#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# 

# ##  1. List of tuples

# ### i. Change element of a single tuple.
Changing element of a Single tuple is not be possible because it posses Immutable behaviour, but it is possible with help 
of converting the tuple into the List forcefully and the again convert it into tuple which will alter its behaviour of immutablity.

# In[6]:


tuple1 = ('1', '2', '3', '4', '5')
list1 = list(tuple1)                   #conversion of tuple to list
list1[3] = '1818'                      #Placing 1818 at the place of index 3
tuple2 = tuple(list1)                  #conversion of list to tuple again
print("Tuple Before Convert:",tuple1)
print("Tuple After Convert:",tuple2)


# ### ii. Change the entire tuple.

# In[13]:


tuple1 = [(1,2),(2,1),(32,12)]
tuple1[1]=(22,18)                    #changing tuple at 1st index with (22,18)
print(tuple1)


# ## 2. Tuple of Lists

# ### i. Change element of a single list

# In[17]:


tuple1=([5,4,3,2,1],[1997],["rutesh","rathod"])
tuple1[2][0]="rowdy"                #Changing single element at [2][0] index.
print(tuple1)


# ### ii. Change the entire list
Changing of entire list inside a tuple is not possible as they are array but single elements can be changed.
# ## 3. What is namedtuple in python?

# In[ ]:





# ## 4. Find smallest second index value from a list of tuples

# In[25]:


x = [(3, 1), (4, 2), (9, 0), (6, -2),  (-9, -1)]
msum=0
minv=0
for element in x:
    if element[1]<minv:              #comparisson of every second index value with previous smallest value
        minv=element[1]
        
        
print("smallest second index value", minv)    


# ## 5. Find the list in a list of lists whose sum of elements is the highest
# 

# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 
# 
# Output: [10, 11, 12]

# In[51]:


great=0

val=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

for i in val:
    x=sum(i)
    if great<x:
        great=x
        max=i
print(max)

    


# In[ ]:





# In[ ]:




