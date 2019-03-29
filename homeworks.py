# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:57:25 2019

@author: Ilmarsl
"""



#Homework nr. 1
#
# Papildiunāts ar to ka rezultāts tiek ierkastīts failā
def writeFile(filename):
    filename = input('Enter File name:')
    with open(filename+'.txt', mode='w') as fout:
        datalist = list(range(1,101))
        # datalist[5]='Fizz'
        for n in datalist:
            text=n
            if n==5:
                text = 'Fizz'
            if n==7:
                text = 'Buzz'
            if n==35:
                text = 'FizzBuzz'
            fout.write(f'n: {text} \n')
print("Homework Nr. 1")
print("FizzBuzz task, result will be writen in to file")
writeFile('fizzbuzz')



# Homework Nr. 2
# Easy
# Write a function to calculate volume for Rectangular Cuboid (visas malas ir taisnsturas 3D objektam)
def getRectVol(l,w,h):
    return l*w*h #You should be returning something not None!
print("Homework Nr. 2")
print("Write a function to calculate volume for Rectangular Cuboid ")
print("Check getRectVol(2,5,7) == 70: ", getRectVol(2,5,7) == 70)


# Homework Nr. 3
# Medium
# Write a function to check if string is a palindrome
def isPalindrome(s):
    sList = list(s)
    sList.reverse()
    revString = ''.join(sList)
    return True if revString == s else False

print("Homework Nr. 3")
print("Write a function to check if string is a palindrome ")

print("Check: isPalindrome('alusariirasula') == True: ", print(isPalindrome('alusariirasula') == True))
print("Check: isPalindrome('normaltext') == False: ", isPalindrome('normaltext') == False)



# Homework Nr. 4
# One liner is possible! Okay to do it a longer way
# Hints: dir("mystring") for string manipulation(might need more than one method)
# Also remember one "unique" data structure we covered

#var jau to ierkastīt vienā rindiņā, bet tad sanāk nepārskatāmi
import string
def isPangram(string, a=string.ascii_lowercase):
    dif = set(a).difference(set(string))
    return True if len(dif) == 0 else False

print("Homework Nr. 4")
print("Write a function to calculate volume for Rectangular Cuboid ")
#tests
assert(isPangram('dadfafd') == False)
assert(isPangram("The quick brown fox jumps over the lazy dog") == True)
#assert(isPangram("The five boxing wizards jump quickly") == True)
print(isPangram("The quick brown fox jumps over the lazy dog"))
print(isPangram('dadfafd'))