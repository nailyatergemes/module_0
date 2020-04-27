#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

while True:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count += 1                     # плюсуем попытку
    if number == predict: break    # выход из цикла, если угадали
    elif number > predict: print (f"Угадываемое число больше {predict} ")
    elif number < predict: print (f"Угадываемое число меньше {predict} ")
        
print (f"Вы угадали число {number} за {count} попыток.")


# In[2]:


import numpy as np
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")
for count in range(1,100):         # более компактный вариант счетчика
    if number == count: break    # выход из цикла, если угадали      
print (f"Вы угадали число {number} за {count} попыток.")


# In[3]:


# добавьте функцию get_euro_rate
import random
def get_euro_rate():
    rand2 = random.randrange(65, 85)
    return rand2
# используйте get_euro_rate в следующей функции
def to_euro(price):  
    get_euro_rate()
    rounded = round(get_euro_rate, 2)  
    return '€' + str(rounded)


# In[4]:


values = [4, 8, 15, 16, 23, 42]
mean = 18

result = map(lambda x: x-mean, values)


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




