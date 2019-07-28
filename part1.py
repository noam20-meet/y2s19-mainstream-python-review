# Part 1 of the Python Review lab.

def hello_world():
	return("hello world")
hi =hello_world()

def greet_by_name(name):
	return("hello"+ " "+name)
# greet= greet_by_name("hello "+ str(name))
greet = greet_by_name("noam")


def encode(x):
	return(x * 3953531)
number=encode(5)

def decode(x):
	return (x/3953531)
result= decode(number)
print(number, result)


	
