# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


# The first 19 numbers are unique
# Have a blank string for zero because we don't say twenty zero, we say twenty
# and it makes strings convenient because index 1 is "one", index 9 is "nine", etc
first_nine = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# ten_teens contains all the weird numbers between 10 and 19 (inclusive)
ten_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# Each 10s is unique too
# Skip 0 and 10 so that indices are easier to work with
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#determines whether or not we want spaces when forming the number string (this is only for readability)
space = ""
# This only takes numbers up to 1000
def num_to_str(num):
	num_str = ""
	while num > 0:
		if num == 1000:
			return "one" + space + "thousand"
		elif num < 1000 and num >= 100:
			hundreds_digit = num // 100
			num_str += first_nine[hundreds_digit] + space + "hundred" + space
			num %= 100
			# we have to put "and" when we have a number that isn't divisible by 100
			if num != 0:
				num_str += "and" + space
		# numbers below 20 are unique, so handle those cases separately
		elif num < 100 and num >= 20:
			tens_digit = num // 10
			num_str += tens[tens_digit] + space
			num %= 10
		elif num < 20 and num >= 10:
			ones_digit = num % 10
			num_str += ten_teens[ones_digit]
			num = 0
		elif num < 10:
			num_str += first_nine[num]
			num = 0
	return num_str

# Test cases
print("Printing test cases:")
print(1, num_to_str(1))
print(5, num_to_str(5))
print(10, num_to_str(10))
print(15, num_to_str(15))
print(19, num_to_str(19))
print(20, num_to_str(20))
print(25, num_to_str(25))
print(99, num_to_str(99))
print(100, num_to_str(100))
print(170, num_to_str(170))
print(171, num_to_str(171))
print(900, num_to_str(900))
print(999, num_to_str(999))
print(1000, num_to_str(1000))

# Result
print("\n\nCalculating result:")
space = ""
answer = sum([len(num_to_str(num)) for num in range(1001)])
print("Answer is", answer)

# If you want to see the actual output
show_output = False
if show_output:
	agg_len = 0
	for num in range(1001):
		current_str = num_to_str(num)
		current_len = len(current_str)
		ans += current_len
		print("length of\t", current_str, "\t\t", current_len, "aggregate length\t", agg_len)