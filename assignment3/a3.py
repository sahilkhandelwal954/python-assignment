#5.Write a Python function called multiplication_table that takes an
# integer n as input and prints the multiplication table of n up to 10.

num = int(input("multiplication of table   "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
    