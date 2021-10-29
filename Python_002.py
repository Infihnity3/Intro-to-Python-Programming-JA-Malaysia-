import numpy as np

height = [1.7, 1.6, 1.5, 1.3, 1.6]
np_height = np.array(height)

weight = [40, 50, 60, 60, 70]
np_weight = np.array(weight)

print(np_height)
print(np_weight)

bmi = np_weight/np_height**2

print(bmi > 20)
