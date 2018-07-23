def methodception(another):
	return another()

def add_two_numbers():
	return 35 + 77

#print(methodception(add_two_numbers))

#Lambda functions are always in one line

#print(methodception(lambda: 35 + 77))

#lambda
my_list  = [13, 56, 77, 484]
print(list(filter(lambda x : x != 13, my_list)))

#normal function
def not_thirteen(x):
	return x != 13
print(list(filter(not_thirteen,my_list)))

#list comprehension
print([x for x in my_list if x != 13])
