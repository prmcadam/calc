import sys

def add_all(nums):
	return sum(nums)

def multiply_all(nums):
	return reduce(lambda a, b: a*b, nums)

if __name__ == '__main__':
	command =sys.argv[1]
	nums=sys.argv[2:]
	if command=='add':
		print add_all(nums)
	if command=='multiply':
		print multiply_all(nums)
