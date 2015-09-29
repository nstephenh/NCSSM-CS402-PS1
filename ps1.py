#################################################
#  Author: Noah Haskell
#  Date: September 27, 2015
#  URL: https://github.com/nstephenh/NCSSM-CS402-PS1
#  PS1.py
#################################################
#This code can be found on github at https://github.com/nstephenh/NCSSM-CS402-PS1

##put any imports at the top of this file (right here is fine)
import random

##if you define any helper functions, put them here and give 
##them a docstring.

def yearify(yearnoformat):
	"""Precondition: yearnoformat is a 2 or 4 letter string containing a year
	Postcondition: Return the year as a 4 letter string
"""	
	if len(yearnoformat) == 2 :
		if int(yearnoformat) < 15:
			return "20" + yearnoformat
		else:
			return "19" + yearnoformat
	else: 
		return yearnoformat 

def meanie(theList):
	"""Precondition: theList is a non-empty list of numbers
Postcondition: return the mean of the numbers."""
	total = 0
	for item in theList:
		total = total + item
	mean = sum / len(theList)		
	return mean

def datePlus(theDate):
	"""Precondition: theDate is a string containing a date.  
Postcondition: Return the sum of the year, month, and day.  You must accept any of the following formats of dates.  You may assume that any year smaller than 15 is preceeded by 20 and any year larger than 15 is preceded by 19.
dd/mm/yyyy
dd-mm-yyyy
ddmmyyyy
ddmmyy
dd/mm/yy
dd-mm-yy

"""
	if theDate[2] == "-" or theDate [2] == "/":
		return int(theDate[0:2]) + (int(theDate[3:5]) ) + int(yearify(theDate[6:]))
	else:	
		return int(theDate[0:2]) + int(theDate[2:4]) + int(yearify(theDate[4:]))

#here are some tests to implement.
#print ("""datePlus("01/01/1970")""" + str(datePlus("01/01/1970") == 1972))
#print (datePlus("08/12/1995") == 2015 )
#print (datePlus("08/12/95") == 2015)
#print (datePlus("08/12/14") == 2034)

#Challenge question:  Why did we nest the if statements this way?
#Can you develop a solid reason?  This is free code for the problems
#below.
###################FREE CODE######################################
def isLeap(year):
    """prec:  year is a modern year
postc: returns True if the year leaps.
"""
    out = False
    if year %4 == 0:
        out = not out
        if year % 100 == 0:
            out = not out
            if year % 400 == 0:
                out = not out
    return out
##############END FREE CODE######################################


def dayInYear(year, month, day):
	"""prec:  year/month/day is a valid date
	postc: returns the ordinal position of the day in the year
	(Feb 15 is the 46th day of year 2000).
	Hint:  sum is your friend"""
	isleap = int(isLeap(year))
	dayspermonth = [31, (isleap + 28), 31, 30 , 31, 30 , 31, 31, 30, 31, 30 , 31]
	return (sum(dayspermonth[:month-1]) +day)

def daysLeftInYear(year, month, day):
	"""prec:  year/month/day is a valid date
	postc: returns the number of days left in the year
	(Feb 15 is the 46th day of year 2000)."""
	lengthOfYear = 365
	if isLeap(year):
		lengthOfYear +=1
	return (lengthOfYear - dayInYear(year, month, day))

def daysToGraduation(month, day):
	"""prec:  year/month/ is a valid date in 2016 before graduation
	postc: returns the number of days until graduation
	"""
	#may 28, 2016
	return dayInYear(2016, 5, 28) - dayInYear(2016, month, day)
	

def dhms(secs):
	"""prec:  secs is a nonnegative integer
postc: return a STRING of the form d:hh:mm:ss, where
d is the number of days, h is the number of hours, m is the number     of minutes, and s is the number of seconds, h < 24, 0 <= m, s, < 60.
Give h, m, s a two character width, padding with zeroes as needed.
"""
	d, h, m, s = "0","0","0","0" 
	if secs/(60*60*24) >= 1:
		d = str(int(secs/(60*60*24)))
		secs = secs % (60*60*24)
	if secs/3600 >= 1:
		h = str(int(secs/3600))
		secs = secs % 3600	
		if len(h) == 1:
			h = "0" + h
	if secs/60 >= 1:
		m = str(int(secs/60))
		secs = secs % 60
		if len(m) == 1:
			m = "0" + m
	s = str(secs)
	if len(s) == 1:
		s = "0" + s
	return ( d + ":" + h + ":"+ m + ":" + s )


def waterCloset(theString):
	"""precondition: thesString is a string.
postcondition: a tuple (c, w, l) where c is the number of characters in 
theString, w is the number of words, and l is the number of lines in the string"""
	return (len(theString),len(theString.split()), len(theString.split("\n")))

def mathCase(x):
	"""precondition: x is a number
postcondition: If x > 4, f(x) = x - 4, if x < -5, f(x) = x + 5,
otherwise, f(x) = 0."""
	if x > 4:
		return x -4
	elif x < -5:
		return x + 5
	return 0



if __name__ == "__main__":
	# Code to test datePlus
	failures = 0
	for yone in range(19, 20): # For each year that starts with 19 or 20
			for ytwo in range(0,99): # the rest of the date
				yone = str(yone)
				ytwo = str(ytwo)
				if len(ytwo) == 1:
					ytwo = "0" + ytwo
				yfour = yone + ytwo
				for m in range(1,12): # And each month in that year
					maxdays = 31
					if m in [9, 4, 6, 11]:
						maxdays = 30  #September, april June and November
					elif m == 2: #February Handling
						if isLeap(int(yfour)):
							maxdays = 29
						else:
							maxdays = 28
					m = str(m)
					if len(m) == 1:
						m = "0" + m				
					for d in range(1,maxdays): # and each day in that month
						d = str(d)
						if len (d) == 1:
							d = "0" + d
						cases = []
						for seperator in ["", "/", "-"]:
							cases.append(m + seperator + d + seperator + yfour)
						for case in cases: # and each way of writing that month
							if (int(m) + int(d) + int(yfour)) != datePlus(case): #check and see if the sum is right
								print ("Failure for case " + case)
								failures +=1
						cases = []
						for seperator in ['', '/', '-']:
							cases.append(m + seperator + d + seperator + str(ytwo))
						for case in cases:
							if (int(m) + int(d) + int(yearify(ytwo))) != datePlus(case):
								print ("Failure for case " + case)
								failures +=1
	print("The following number is the number of dates that produced errors between 1900 and 2099: " + str(failures))


	#code to test daysinyear
	print("dayInYear(2000,02,15) == 44 returns " + str(dayInYear(2000, 2, 15) == 46))
	#code to test daysLeftInYear
	print("dayLeftInYear(2000, 8, 21) == 132 returns " + str(daysLeftInYear(2000, 8, 21) == 132))
	#code to test daysTillGraduation
	print("daysToGraduation(5, 23) == 5 returns " + str(daysToGraduation(5, 23) == 5))
	# code to test dhms
	print ("dhms(273602) should be  '3:04:00:02' and is " + str(dhms(273602)))
	print ("dhms(311023) should be  '3:14:23:43' and is " + str(dhms(311023)))
	# code to test watercloset
	print ("waterCloset('This \nis \nSparta!!!!') should be (22, 3, 3) and is " +  str(waterCloset('This \nis \nSparta!!!!')))
	# code to test mathCase
	print ("mathCase(6) should be  2 " + str(mathCase(6) == 2))
	print ("mathCase(4) should be  0 " + str(mathCase(4) == 0))
	print ("mathCase(-6) shoud be -1) " + str(mathCase(-6) == -1))
