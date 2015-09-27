#################################################
#  Author:
#  Date:
#  PS1.py
#################################################
#  There is a bonus for getting this in early!

#If you get help on this assignment, you must report who you received #help from and on what you received help with.
#Fill out the comment box at the top under or suffer the pain of #death and endless heckling.

##put any imports at the top of this file (right here is fine)

##if you define any helper functions, put them here and give 
##them a docstring.

def meanie(theList):
    """Precondition: theList is a non-empty list of numbers
Postcondition: return the mean of the numbers."""
    return 0

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
    pass
#here are some tests to implement.
datePlus("01/01/1970") == 1972
datePlus("08/12/1995") == 2015
datePlus("08/12/95") == 2015
datePlus("08/12/14") == 2034

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
    (Feb 15 is the 44th day of year 2000).
    Hint:  sum is your friend"""
    return 0

def daysLeftInYear(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the number of days left in the year
    (Feb 15 is the 44th day of year 2000)."""
    return 0

def daysToGraduation(month, day):
    """prec:  year/month/ is a valid date in 2015 before graduation
    postc: returns the number of days until graduation
"""
    return 0

def dhms(secs):
    """prec:  secs is a nonnegative integer
    postc: return a STRING of the form d:hh:mm:ss, where
    d is the number of days, h is the number of hours, m is the number     of minutes, and s is the number of seconds, h < 24, 0 <= m, s, < 60.
Give h, m, s a two character width, padding with zeroes as needed.
"""
    return ""



def waterCloset(theString):
    """precondition: thesString is a string.
postcondition: a tuple (c, w, l) where c is the number of characters in 
theString, w is the number of words, and l is the number of lines in the string"""
    return (0,0,0)

def mathCase(x):
    """precondition: x is a number
postcondition: If x > 4, f(x) = x - 4, if x < -5, f(x) = x + 5,
otherwise, f(x) = 0."""
    return 0




if __name__ == "__main__":
    pass
    ##put test code here and get rid of the pass statement.
    ##Writing good test code helps your grade! And it prevents
    ## you from making stupid mistakes. 
