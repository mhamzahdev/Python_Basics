print("Enter radius of Circle")
radius = float(input())
area = 3.14*radius*radius
# print(area)
area = str(area)
print("Area of circle is " + area)      # it will give error if you dont typecast because in python you cannot concatenate String with float