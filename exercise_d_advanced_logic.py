# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 



# 1...
print([x for x in numbers if x%2==0])

# 2...
print(max(numbers) - min(numbers))

# 3...
for i in range(1, len(numbers)):
	if numbers[i] == numbers[i-1]:
		print(True)

# 4...
sum = 0
ignore = False
for i in range(len(numbers)):
	if numbers[i] == 6:
		ignore = True
		continue
	if numbers[i] == 7:
		ignore = False
		continue
	if ignore:
		continue
	sum += numbers[i]
#	print(" added")
print(sum)

# 5...
sum = 0
ignoreNext = False
for i in range(len(numbers)):
	if numbers[i] == 13:
		ignoreNext = True
		continue
	if ignoreNext:
		ignoreNext = False
		continue
	sum += numbers[i]
print(sum)