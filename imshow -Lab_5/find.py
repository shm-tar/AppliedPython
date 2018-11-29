import numpy as np

a = np.random.randint(0, 10000, size=(209, 29))

print(a)


def find(array, value):
    found = array[abs(array - value) == abs(array - value).min()]
    return found


print(find(a, 4732))
