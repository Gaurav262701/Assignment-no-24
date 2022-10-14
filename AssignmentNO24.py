#!/usr/bin/env python
# coding: utf-8

# # Assignment 24 Solutions

# 1.Create a function that takes an integer and returns a list from 1 to the given number, where:
# 1.If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
# 2.If the number cannot be divided evenly by 4, simply return the number.

# In[2]:


def amplify(in_num):
    out_list = []
    for i in range(1,in_num+1):
        if i % 4 == 0:
            out_list.append(i*10)
        else:
            out_list.append(i)
    print(f'{in_num}-->{out_list}')
    
amplify(4)
amplify(3)
amplify(25)


# 2.Create a function that takes a list of numbers and return the number that's unique.

# In[3]:


def unique(in_list):
    out_num = ''
    for i in set(in_list):
        if in_list.count(i) == 1:
            out_num = i
    print(f'{in_list}-->{out_num}')
    
unique([3,3,3,7,3,3,3])
unique([0,0,0.77,0,0])
unique([0,1,1,1,1,1,1])


# 3.Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference). For help with this class, I have provided you with a Rectangle constructor which you can use as a base example ?

# In[5]:


import math
class Circle:
    def __inti__(self,radius):
        self.radius = radius
    def getArea(self):
        print(f'Radius --> {round(math.pi*self.radius*self.radius)}')
    def getPerimeter(self):
        print(f'Perimeter-->{round(2*math.pi*self.radius)}')
        
circy = Circle(11)
circy.getArea()

circy = Circle(4.44)
circy.getPerimeter()


# 4.Create a function that takes a list of strings and return a list, sorted from shortest to longest.

# In[6]:


def sort_by_len(in_list):
    print(sorted(in_list,key=len))

sort_by_len(["Google","Apple","Microsoft"])
sort_by_len(["Leonardo","Michlengelo","Raphael","Donatello"])
sort_by_len(["Turing","Einstein","jung"])


# 5.Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

# In[7]:


def is_triplet(a,b,c):
    if ((a**2+b**2)==(c**2)):
        print(f'{a,b,c}-->{True}')
    else:
        print(f'{a,b,c}-->{False}')
        
is_triplet(3,4,5)
is_triplet(5,6,7)
is_triplet(1,2,3)


# In[ ]:




