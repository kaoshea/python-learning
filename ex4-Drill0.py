# Shaw writes:
# When I wrote this program the first time I had a mistake, and Python told me about it like this:

# Traceback (most recent call last):
#        File "ex4.py", line 8, in <module>
#           average_passengers_per_car = car_pool_capacity / passenger
#      NameError: name 'car_pool_capacity' is not defined

# Explain this error in your own words. Make sure you use line numbers and explain why.

# My answer:
# There are 2 errors that are apparent right away. First, in line 7, Shaw defines the variable "carpool_capacity," not "car_pool_capacity." Second, in line 4, Shaw defines the variable "passengers," not "passenger."
# Thus, when you run the program, you encounter an error (because the versions of the variable names given in line 8 do not match the variables defined in the lines above it).
# Additionally, the old version of line 8 will also not provide a correct answer for the average number of passengers per car.
