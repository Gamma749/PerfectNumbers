import math
def factors(n):
    """A generator that provides the factors of an integer n"""
    #All numbers have 1 as a factor, needed for perfect numbers -.-
    yield 1
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            #We can be sneaky and give the factors out of order
            #If i is a factor, then so is n//i
            #This cuts computation in half
            yield i
            yield n//i


#Start searching at 2
i = 2
currSum = 0


while True:
    #Create a generator for the current number
    f = factors(i)
    #Loop and add the factors up
    while True:
        try:
            currSum += next(f)
            if currSum>i:
                #If we are already above the number in question, give up
                break
        except StopIteration:
            break
    #End while
    if currSum == i:
        print(f'\n{i} is a perfect number')
        input("Keep searching? ")
    i+=1
    currSum=0
    
