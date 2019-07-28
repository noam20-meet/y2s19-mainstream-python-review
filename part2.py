# Part 2 of the Python Review lab.

def encode(x, y):
	primenum(x,y)
	if 1 < y < 25 and 500 < x < 1000:
		return x*y
		product= encode(643,5)
		coded_message= decode()
	else:
		print("Invalid input: Outside range")

def primenum(x,y):
	if x > 1:
   # check for factors
	   for i in range(2,x):
	       if (x % i) == 0:
	           print(x,"is not a prime number")
	           print(i,"times",x//i,"is",x)
	           x+=1

	   else:
	       print(x,"is a prime number")

	if y > 1:
   # check for factors
	   for i in range(2,y):
	       if (y % i) == 0:
	           print(y,"is not a prime number")
	           print(i,"times",y//i,"is",y)
	           y+=1
	   else:
	       print(x,"is a prime number")
		
		



def decode(coded_message):
	pass
	