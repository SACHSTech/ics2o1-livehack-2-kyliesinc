
# title
print ("***Welcome to Triangle Checker***")

# get the triangle sides
side_1 = float(input("Enter the length of the first side: "))
side_2 = float(input("Enter the length of the second side: "))
side_3 = float(input("Enter the length of the third side: "))

# Determine which side is the largest
if (side_1 >= side_2) and (side_1 >= side_3):
   largest = side_1
elif (side_2 >= side_1) and (side_2 >= side_3):
   largest = side_2
else:
   largest = side_3

# Determine if the figure creates a triangle or not
if largest == side_1:
  if side_2 + side_3 > side_1:
    print ("This figure is a triangle.")
  else:
    print ("This figure is NOT a triangle.")
elif largest == side_2:
  if side_1 + side_3 > side_2:
   print ("This figure is a trianlge.")
  else:
    print ("This figure is NOT a triangle.")
elif largest == side_3:
  if side_1 + side_2 > side_3:
    print ("This figure is a triangle.")
  else:
    print ("This figure is NOT a triangle.")

