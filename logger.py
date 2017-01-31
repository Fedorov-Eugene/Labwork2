class tracer(object):
	def __init__(self, func): 
		self.calls = 0
		self.func = func
		self.args = 0
		self.res = dict()
		self.name = self.func.__name__

	def __call__(self, *args): 
		self.calls += 1
		self.args = args
		if self.res.get(str(self.args)):
			return self.res[str(self.args)]
		else:
			self.res[str(self.args)] = self.func(*args) 
			return self.res[str(self.args)]

	def __get__(self, instance, owner): 
		def wrapper(*args): 
			return self(instance, *args)
		return wrapper

	def __str__(self):
		return "Вызвали {} раз, функция - {}, аргументы и результаты - {}".format(self.calls, self.name, self.args, self.res)


class test(object):
	def __init__(self):
		self.num = 0

	@tracer
	def test(self, a):
		return(a*10)



@tracer
def kek(a, b, c):
	return a+b+c

if __name__ == '__main__':
	kek(1,2,3)
	kek(3,4,5)
	kek(1,2,3)
	print(str(kek))


	t = test()
	t.test(10)
	t.test(20)
	t.test(10)
	print(str(t.test))