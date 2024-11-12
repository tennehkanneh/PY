# the string is an object
course = 'Python For Beginners'

# when a function is part of an object it is reffered to as a method

#upper method
print(course.upper())
print(course)

# lower method
print(course.lower())
print(course)

#find method
# finds the index of the first character instance of y
# Would return a -1 if not found (ex. 'Y')
print(course.find('y'))
print(course)


# replace method
# replace any 'n' in course with an 's'
print(course.replace('n', 's'))
print(course)

# strings are remudiable 
# any time you try to change a string you will create another one in memorey

# this expression checks to see if 'Python' is in the course string
print('Python' in course)