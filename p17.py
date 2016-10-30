# The first 19 numbers are unique
first_nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# ten_teens contains all the weird numbers between 10 and 19 (inclusive)
ten_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# Each 10s is unique too
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
# After those, 20 through 29 are the same as 90-99

# slight inefficiency since this has to create a whole list just to sum them
def get_length_strings(array):
	return sum([len(num) for num in array])

# Length from 1-9
first_nine_length = get_length_strings(first_nine)
print("length first nine", first_nine_length)

# 20-99, we just find the length of the tens and then multiply it by 10 because each level of 10 occurs 10 times
# i.e. twenty, twenty one ... twenty nine
tens_length = get_length_strings(tens) * 10
# And then we need to find the second digit, which is just the same as the first nine for each tens
tens_length += first_nine_length * len(tens)

# Now take into account the length from 10-19
ten_teens_length = get_length_strings(ten_teens) 
tens_length += ten_teens_length
print("length tens", tens_length)

# 100-999
# first digit (and don't forget about "and")
# find number of "hundreds" there are from 100-999 inclusive
# one hundred, one hundred and one ... one hundred and ninety nine
# Note that "and" doesn't appear for the first entry
hundreds_length = sum([len("hundred") + len(num) * 100 for num in first_nine]) + len("and") * (100 - 1) * 9
# hundreds_length = first_nine_length + len("hundred") + len("and") * (999 - 100 + 1)
hundreds_length += tens_length + first_nine_length * 9
print("length hundreds", hundreds_length)

thousands_length = len("onethousand")

print("length thousands", thousands_length)

total_length = first_nine_length + tens_length + hundreds_length + thousands_length
print("length total up to one thousand", total_length)