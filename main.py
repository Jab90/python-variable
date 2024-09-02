'''
Variable Assignment
'''

# add 'Jabbeer' to the variable 'name'
# name = "Jabbeer"
# print(name)

# ===================

# assign same value to multiple variables on the same line
a = b = c = 'Cat'
print(a)
print(b)
print(c)

# ===================

# reuse variable names, the last assignment is printed
# colour = 'Red'
# colour = 'Blue'

# print(colour)

# ===================

# legal names
# firstname = 'Jabbeer'
# first_name = 'Jabbeer'
# _first_name = 'Jabbeer'
# firstName = 'Jabbeer'
# first_name2 = 'Jabbeer'
# FIRSTNAME = 'Jabbeer'

# # illegal variable names
# 2firstname = 'Jabbeer'
# first-name = 'Jabbeer'
# first name = 'Jabbeer'

# ===================

'''
Reserved Keywords
'''
# help("keywords")

# from = "London"
# print(from)

# ===================

# Variable Types
# var = "Hello World"
# print(type(var))

# var = 23
# print(type(var))

'''
Object Indentity
'''
# score = 400
# identity = id(score)
# print(identity)

# ===================

# score variable is saved into the pb by reference

# score = 400
# pb = score
# print(id(score))
# print(id(pb))

'''
Object Reference
'''

# both score and pb point to the same into object
# score -----> int 100 <----- pb
# score = 100
# pb = score

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

# ===================

# pb ---------> int 20
# score --------> int 100
# pb = 20 
# score = 100 

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

# ===================
# garbage collection

# pb ---------> int 20
# score --------> str 'Completed'
#       -----------> int 100

# pb = 20 
# score = 100
# score = 'Completed'

# print(type(score))
# print(type(pb))
# print(score)
# print(pb)
