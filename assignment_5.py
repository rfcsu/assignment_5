"""
Course: CSC500-1
Module: 5
Date: Aug 13, 2024
"""

# Problem 1
def problem_1():
	def j_to_month(j):
	    return {
	        0: 'January',
	        1: 'February',
	        2: 'March',
	        3: 'April',
	        4: 'May',
	        5: 'June',
	        6: 'July',
	        7: 'August',
	        8: 'September',
	        9: 'October',
	        10: 'November',
	        11: 'December'
	    }[j]

	acc = 0
	yrs = int(input('Enter the number of years: '))

	for i in range(yrs):
	    for j in range(12):
	        while True:
	            try:
	                _input = int(input(f'Enter the amount of rain in {j_to_month(j)} for year {i+1}: '))
	                acc += _input
	                break
	            except ValueError:
	                print(f'Invalid Input Error: Please enter a valid whole number for inches of rainfall.')
	                exit(1)

	total_months = yrs * 12
	avg = acc / total_months

	print(f'\nNumber of months: {total_months}')
	print(f'Total inches of rainfall: {acc}')
	print(f'Average rainfall per month over {yrs} years: {avg:.2f} inches')



# Problem 2
def problem_2():
	def points(p):
	    if p >= 8:
	        return 60
	    elif p >= 6:
	        return 30
	    elif p >= 4:
	        return 15
	    elif p >= 2:
	        return 5
	    else:
	        return 0

	try:
	    _input = int(input('How many books did you purchase this month at the bookstore? '))
	    print(f'You accumulated {points(_input)} points!')
	except ValueError:
	    print(f'Invalid Input Error: Your input is not a valid whole number.')


if __name__ == '__main__':
	problem_1()
	problem_2()