#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  s=a+b
  if(a==10 or b==10 or s==10):
    return True
  else:
    return False
  
makes10(9, 10)
makes10(9, 9)
makes10(1, 9)
