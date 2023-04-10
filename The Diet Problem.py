#!/usr/bin/env python
# coding: utf-8

# In[98]:


get_ipython().run_line_magic('config', 'Completer.use_jedi = True')
from pulp import *


# In[99]:


#Creating a food object that will store facts about the various foods in my diet 

class Food:
    def __init__(self, name: str, cost: float, calories: int, sodium: int, protein: float, 
                 vitaminD: float, calcium: int, iron: float, potassium: int):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.sodium = sodium
        self.protein = protein
        self.vitaminD = vitaminD
        self.calcium = calcium
        self.iron = iron
        self.potassium = potassium
        


# In[100]:


#Defining my 5 food items 

blackberry = Food('blackberry', 2.12, 72, 1, 1.2, 1, 50.4, 1.068, 280)
frozenDinner = Food('frozen dinner', 2.98, 340, 760, 17.0, 1, 50, 1.80, 500)
ketoCereal = Food('keto cereal', 1, 110, 90, 10.0, 1, 50, 1.1, 20)
proteinBar = Food('protein bar', 1.75, 140, 100, 12.0, 1, 220, 1, 89)
ribeye = Food('ribeye steak', 18.87, 400, 60, 18.0, 1, 32, 6.5, 757)

mainDiet = [blackberry, frozenDinner, ketoCereal, proteinBar, ribeye]


# In[101]:


# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Diet Problem", LpMinimize)

# Create a dictionary 'food_vars' to contain the LpVariable objects
food_vars = LpVariable.dicts("Foods", mainDiet, lowBound=0, cat='Continuous')

# Add the objective function to the 'prob' variable
prob += lpSum([food.cost * food_vars[food] for food in mainDiet]), "Total Cost"

# Add the constraints to the 'prob' variable
prob += lpSum([food.calories * food_vars[food] for food in mainDiet]) >= 2000, "Minimum Calories"
prob += lpSum([food.sodium * food_vars[food] for food in mainDiet]) <= 5000, "Maximum Sodium"
prob += lpSum([food.protein * food_vars[food] for food in mainDiet]) >= 50, "Minimum Protein"
prob += lpSum([food.vitaminD * food_vars[food] for food in mainDiet]) >= 20, "Minimum Vitamin D"
prob += lpSum([food.calcium * food_vars[food] for food in mainDiet]) >= 1300, "Minimum Calcium"
prob += lpSum([food.iron * food_vars[food] for food in mainDiet]) >= 18, "Minimum Iron"
prob += lpSum([food.potassium * food_vars[food] for food in mainDiet]) >= 4700, "Minimum Potassium"


# In[102]:


# Solve the optimization problem
prob.solve()

# Print the status of the solution
print("Status: {}".format(LpStatus[prob.status]))

totalCost = 0
# Print the optimal solution
for food in mainDiet:
    print(food.name, ":", food_vars[food].varValue, '- Cost: $', round(food_vars[food].varValue* food.cost,2) )
    
    totalCost = totalCost + (food_vars[food].varValue* food.cost)

print('$',round(totalCost,2))


# In[95]:


#I don't really like the taste of protein bars. Let's drop it from my main diet 
newDiet = [blackberry, frozenDinner, ketoCereal, ribeye]

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Diet Problem", LpMinimize)

# Create a dictionary 'food_vars' to contain the LpVariable objects
food_vars = LpVariable.dicts("Foods", newDiet, lowBound=0, cat='Continuous')

# Add the objective function to the 'prob' variable
prob += lpSum([food.cost * food_vars[food] for food in newDiet]), "Total Cost"

# Add the constraints to the 'prob' variable
prob += lpSum([food.calories * food_vars[food] for food in newDiet]) >= 2000, "Minimum Calories"
prob += lpSum([food.sodium * food_vars[food] for food in newDiet]) <= 5000, "Maximum Sodium"
prob += lpSum([food.protein * food_vars[food] for food in newDiet]) >= 50, "Minimum Protein"
prob += lpSum([food.vitaminD * food_vars[food] for food in newDiet]) >= 20, "Minimum Vitamin D"
prob += lpSum([food.calcium * food_vars[food] for food in newDiet]) >= 1300, "Minimum Calcium"
prob += lpSum([food.iron * food_vars[food] for food in newDiet]) >= 18, "Minimum Iron"
prob += lpSum([food.potassium * food_vars[food] for food in newDiet]) >= 4700, "Minimum Potassium"


# Solve the optimization problem
prob.solve()

# Print the status of the solution
print("Status: {}".format(LpStatus[prob.status]))

totalCost = 0
# Print the optimal solution
for food in newDiet:
    print(food.name, ":", food_vars[food].varValue, '- Cost: $', round(food_vars[food].varValue* food.cost,2) )
    totalCost = totalCost + (food_vars[food].varValue* food.cost)

print('$',round(totalCost,2))

