import math         #Importing a built-in module
print("Square root of 49:",math.sqrt(49))       #Using a built-in module function
from math import pow        #Importing a specific function from a module
print("2 to the power 5:", pow(2,5))

"""
pip is used to install external Python modules.
Example (run in terminal / command prompt, not in Python file): pip install requests
"""

'''✅ Assignment:❤️
Use Python modules and pip-installed libraries to perform basic QA/testing-related tasks such 
as generating test data and validating results.'''

#🚀 Try it yourself first before scrolling down to see the solution!


import random       #Importing a built-in module for test data preparation
test_id = random.randint(1000,8000)
print("Generated Test ID:", test_id)