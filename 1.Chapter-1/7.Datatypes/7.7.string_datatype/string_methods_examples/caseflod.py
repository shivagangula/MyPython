"""
- The casefold() method returns a string where all the characters are in lower case. 
- It is similar to the lower() method, but the casefold() method converts more characters into lower case.
- For example, the German lowercase letter 'ß' is equivalent to 'ss'. 
Since it is already lowercase, the lower() method would not convert it; whereas the casefold() converts it to 'ss'.
- Use the casefold() method if your application supports globalization or localization.
"""

#ecample (Differance between lower(), casefold() ):
mystr = 'außen'
mystr = 'außen'
print(mystr.casefold())
print(mystr.lower())

#output : aussen
#output : außen

