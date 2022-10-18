#!/usr/bin/env python
# coding: utf-8

# ### Report on (18 October 2022)

# THE PROBLEM\
# The  problem we did in class was that suppose you have coins of value  a and b cents were $a,b \in \mathbb{N}$. Then what amount of money can you get from the combination of these coins?\
# What amount amount of money you cannot have from a,b? 
# 
# From the first glace we see that the multiplies of a  and b should there in the combination.The  example is as follows \
# Lets look at the examples where $a=2$ and $b=3$.n here stands for the number of the coins
# 
# for n = 1 $\quad$   [3,2,5,]
# 
# for n = 2  $\quad$  [3,2,5,6,8,7,4] 
# 
# for n = 3  $\quad$ [3,2,5,6,8,7,4,9,15,11,13,10]  
# 
# The conjecture was that given any n  {now standing  for any amount} using coins a and b it can be expressed as a linear combination of a and b like this:
# 
# n = ax +by  where x,y $\in \mathbb{N} $
# This is the conjecture now
# 
# Lets test this for numbers from  1 to 100. First lets start  with a=2 and b= 3
# 
# n= 5  $\quad$ we have $ 2*1+3*1$
# 
# n= 6   $\quad$ we have $ 2*0+3*2$
# 
# n= 7   $\quad$ we have $ 2*2+3*1$
# 
# n= 8  $\quad$  we have $ 2*4+3*0$
# 
# n= 9 $\quad$ we have $ 2*0+3*3$
# 
# n= 10 $\quad$ we have $ 2*2+3*2$
# 
# n= 11  $\quad$  we have $ 2*1+3*3
#  
# 
# For  the second part let a=3 and b= 5
# 
# n= 3  $\quad$ we have $ 3*0+5*1$
# 
# n= 6   $\quad$ we have $ 3*2+5*0$
# 
# n= 8  $\quad$ we have $ 3*1+ 5*1$
# 
# n= 9  $\quad$ we have $ 3*2+ 5*0$
# 
# n= 10  $\quad$  we have $ 3*0+5*2$
# 
# n= 11  $\quad$ we have $ 3*2+ 5*1$
# 
# n= 12  $\quad$ we have $ 3*4+ 5*0$
# 
# n= 13 $\quad$ we have $ 3*1+5*2$
# 
# n = 14  $\quad$ we have $ 3*3+5*1$
# 
# n= 16 $\quad$ we have $ 3*2+5*2$
# 
# n= 18  $\quad$  we have $ 3*1+5*3$
# 
# For  the second part let a=3 and b= 5
# 
# The code will show it below
# 
# 
# 
# 

# In[11]:


n =  1
a =  int(input("Enter the number a; "))
b =  int(input("Enter the number b: "))
while n<= 100:
    for x in range(0,101):
        for y in range(0,101):
            if (a*x + b*y)==n :
                print('The x value in is',x,'The y value in is',y,"for " ,n)
    n += 1


# In[ ]:




