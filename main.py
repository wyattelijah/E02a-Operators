import utils, random


def add(a1,a2):
    '''
    Adds two numbers together
    '''
    toReturn = 0
    toReturn = a1 + a2
    return toReturn

def sub(a1,a2):
    '''
    Subtracts a2 from a1
    '''
    toReturn = 0
    toReturn = a1 - a2
    return toReturn

def mult(a1,a2):
    '''
    Multiplies a1 by a2
    '''
    toReturn = 0
    toReturn = a1 * a2
    return toReturn

def div(a1,a2):
    '''
    Divides a1 by a2
    '''
    toReturn = 0
    toReturn = a1 / a2
    return toReturn

def floorDiv(a1,a2):
    '''
    Divides a1 by a2 with remainder rounded down
    '''
    toReturn = 0
    toReturn = a1 // a2 
    return toReturn

def mod(a1,a2):
    '''
    Returns the remainder of a1 divided by a2
    e.g., mod(5,3) = 2, mod(15,5) = 0, mod(15,4) = 3
    '''
    toReturn = 0
    toReturn = a1 % a2
    return toReturn

def exp(a1,a2):
    '''
    Returns the a1 to the a2 power (exponent)
    '''
    toReturn = 0
    toReturn = a1 ** a2
    return toReturn

def orderOperations(a1,a2,a3):
    '''
    Returns (a1 plus a2) multiplied by a3
    i.e., changes normal order or operations 
    '''
    toReturn = 0
    toReturn = (a1 + a2) * a3
    return toReturn

def whichType(t):
    '''
    Returns the python data type of t
    '''
    toReturn = ''
    toReturn = type(t)
    return toReturn

def convertInt(i):
    '''
    Converts i to an integer
    '''
    toReturn = 0
    toReturn = int(i)
    return toReturn

def convertFloat(f):
    '''
    Converts f to a float
    '''
    toReturn = 0.0
    toReturn = float(f)
    return toReturn

def convertStr(s):
    '''
    Converts s to a string
    '''
    toReturn = ''
    toReturn = str(s)
    return toReturn

def concat(s1,s2):
    '''
    Concatenates (string) s2 to the end of s1
    '''
    toReturn = ''
    toReturn = s1
    toReturn += s2
    return toReturn

def whichChar(s,a):
    '''
    Returns the character at position a of string s
    '''
    toReturn = ''
    toReturn = s[a]
    return toReturn

def substr(s,a1,a2):
    '''
    Returns a substring of s (from position a1 to a2)
    '''
    toReturn = ''
    i = a1
    while (i < a2) and (i < len(s)):
        toReturn += s[i]
        i += 1
    return toReturn

def reverseStr(s):
    '''
    Returns a string which is a reversed version of s
    '''
    toReturn = ''
    i = len(s) - 1
    while i > -1:
        toReturn += s[i]
        i -= 1
    return toReturn

def isIn(l,e):
    '''
    Returns true if element e is in list l
    '''
    toReturn = ''
    if e in l:
        toReturn = True
    else:
        toReturn = False
    return toReturn

def randomElement(l):
    '''
    Returns a random element of list l
    '''
    toReturn = ''
    toReturn = random.choice(l)
    return toReturn

def randomNumber():
    '''
    Returns a random number between 1000 and 9999
    '''
    toReturn = 0
    toReturn = random.randint(999, 9999)
    return toReturn

def reverseList(l):
    '''
    Returns a list which is a mirror of l (each element is present in reverse order from l)
    '''
    toReturn = []
    i = len(l) - 1
    while i >= 0:
        toReturn.append(l[i])
        i -= 1
    return toReturn

def shuffleList(l):
    '''
    Returns a list which has all the elements of l in a random order
    '''
    toReturn = []
    while l != []:
        item = random.choice(l)
        toReturn.append(item)
        l.remove(item)
    return toReturn

def listUntil(a):
    '''
    Returns a list contains numbers from 0 to a
    '''
    toReturn = []
    i = 0
    if a > 0:
        while i < a:
            toReturn.append(i)
            i += 1
        toReturn.append(a)
    elif a < 0:
        while i > a:
            toReturn.append(i)
            i -= 1
        toReturn.append(a) 
    return toReturn




def main():
    '''
    The main function for this file. It is run if this file is not used as a module.
    '''
    utils.check_version((3,7))          # make sure we are running at least Python 3.7
    utils.clear()                       # clear the screen

    print("Adding some numbers")
    print(add(1,2))
    print(add(1,-2))
    print(add(1.1,5))

    print("Subtracting")
    print(sub(1,2))
    print(sub(1,-2))
    print(sub(1.1,5))

    print("Multiplication")
    print(mult(4,2))
    print(mult(7,-2))
    print(mult(9.3,5))

    print("Division")
    print(div(1,2))
    print(div(10,-2))
    print(div(1.2,5))

    print("Integer or floor division")
    print(floorDiv(1,2))
    print(floorDiv(11,-2))
    print(floorDiv(16.4,5))

    print("Modulo: getting the remainder after division")
    print(mod(15,2))
    print(mod(16,-2))
    print(mod(16.2,5))

    print("Exponents")
    print(exp(10,2))
    print(exp(6,-2))
    print(exp(2.2,5))

    print("Changing the order of operations (with parenthesis)")
    print(orderOperations(1,2,3))
    print(orderOperations(1,-2,-6))
    print(orderOperations(1.5,5,0.2))

    print("Checking data types")
    print(whichType(1))
    print(whichType(1.0))
    print(whichType('1'))
    print(whichType(True))
    print(whichType(False))
    print(whichType((1,2)))
    print(whichType([1,2]))
    print(whichType({1:2}))

    print("Converting to integers")
    print(convertInt(5.2))
    print(convertInt('1'))

    print("Converting to floats")
    print(convertFloat(44))
    print(convertFloat('1'))

    print("Converting to strings")
    print(convertStr(5.2))
    print(convertStr(100))

    print("String concatenation")
    print(concat('This is a ','test'))
    print(concat('Hello,',' World!'))

    print("Slicing")
    print(whichChar('This is a test of the emergency broadcast system.',1))
    print(whichChar('This is a test of the emergency broadcast system.',2))
    print(whichChar('This is a test of the emergency broadcast system.',10))
    print(whichChar('This is a test of the emergency broadcast system.',-1))

    print("Slicing substrings")
    print(substr('This is a test of the emergency broadcast system.',0,100))
    print(substr('This is a test of the emergency broadcast system.',2,5))
    print(substr('This is a test of the emergency broadcast system.',10,12))
    print(substr('This is a test of the emergency broadcast system.',-5,-1))

    print("Reversing strings")
    print(reverseStr('This is a test of the emergency broadcast system.'))
    print(reverseStr('Hello, World!'))

    print("Finding list items")
    print(isIn([1,2,3,4,5,6,7,8],5))
    print(isIn(['A','B','C','D'],'C'))
    print(isIn([1,2,3,4,5,6,7,8],10))
    print(isIn(['A','B','C','D'],'E'))

    print("Returning random list elements")
    print(randomElement([1,2,3,4,5,6,7,8]))
    print(randomElement(['A','B','C','D']))
    print(randomElement(['G','Hello',1.5,(5,5)]))

    print("Random numbers")
    print(randomNumber())
    print(randomNumber())
    print(randomNumber())

    print("Reversing lists")
    print(reverseList([1,2,3,4,5,6]))
    print(reverseList(['a','b','c','d','e','f']))
    print(reverseList(['G','Hello',1.5,(5,5)]))

    print("Randomizing lists")
    print(shuffleList([1,2,3,4,5,6]))
    print(shuffleList(['a','b','c','d','e','f']))
    print(shuffleList(['G','Hello',1.5,(5,5)]))

    print("Making new lists of sequential numbers")
    print(listUntil(10))
    print(listUntil(50))
    print(listUntil(4))
    print(listUntil(-5))

if __name__ == '__main__':
	main()