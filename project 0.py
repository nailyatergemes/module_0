#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[10]:


import numpy as np
number = np.random.randint(1,100) #picking a number between 1 and 100
print ("Загадано число от 1 до 99")
for i in range(1,100):         #counter
    if number == i: break    # exit from cycle if you guessed the number     
print (f"Вы угадали число {number} за {i} попыток.")


# In[ ]:





# In[ ]:




