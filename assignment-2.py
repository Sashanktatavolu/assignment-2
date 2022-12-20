import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 2, 3, 4, 5])

print(s1)
print(s2)
s = s1 + s2
print("Addition is:")
print(s)
print("Subtraction is:")
s = s1 - s2
print(s)
print("Multiplication is:")
s = s1 * s2
print(s)
print("Division is:")
s = s1 / s2
print(s)