# bubble sort

from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
	len_numbers = len(numbers)
	for i in range(len_numbers):
		for j in range(len_numbers - 1 - i):
			if numbers[j] > numbers[j+1]:
				numbers[j] ,numbers[j+1] = numbers[j+1], numbers[j]
	return numbers

if __name__ == '__main__':
	import random
	numbers = [random.randint(0, 1000) for i in range(10)]
	print(f"numbers : {numbers}")
	ans = bubble_sort(numbers)
	print(f"answer : {ans}")
