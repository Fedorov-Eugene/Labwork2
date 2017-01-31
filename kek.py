import random as rnd

def generate(sep = ' ',element = 10,max_str = 100000):

	number_str = '1234567890'

	with open('big_data.txt','w') as f:
		for k in range(max_str):
			num = ''
			for j in range(element):
				num += str(rnd.randint(1,999999999))
				num += sep	
			f.write(num)
	

if __name__ == '__main__':
	generate()	