class Math:
	def add(self, x, y):
		z=x+y
		self.result=z
		return self.result
	def sub(self, x, y):
		z = x-y
		self.result=z
		return self.result
a=Math()
#num1 = input("Enter teh first number:")
#num2 = input("Enter teh second number")
num1 = 10
num2 = 7
d=(a.add(num1, num2))
e=(a.sub(num1, num2))
print('{0},{1}'.format(d,e))
print(d,e)
print(e)
print(d)

