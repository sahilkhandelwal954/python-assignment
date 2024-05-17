# #3.Write a python function called wordCounter that takes a string “S” as an input, and return the count of each character in word or in “S”.
# e.g pass S = “uplfairs pvt ltd”
# u -> 1
# p -> 2
# l ->  2
# and so on

count=0
name="uplfairs pvt ltd"
name=str(input("enter the variable which you want to show:  "))
count +=1
for char in name:
    if char=='s':
        print(char,"------>",count)
    else:
        print("non")