#Problem4.py
#Project Euler problem 4

#from NumberTests import isPalindrome
#from NumberTests import largestPalindrome

def isPalindrome(n):
  pal = str(n)
  if pal == pal[::-1]:
    return True
  else:
    return False 

def largestPalindrome():
  max_pal = 0
  factors = (0, 0) 

  for num1 in range (999, 99, -1):
    for num2 in range (num1, 99, -1):
      product = num1 * num2 
      if product <= max_pal:
        return max_pal, factors 
      if isPalindrome(product):
        max_pal = product
        factors = (num1, num2)  

  return max_pal, factors 

result, (factor1, factor2) = largestPalindrome()
print(result, "=", factor1, "x", factor2) 
