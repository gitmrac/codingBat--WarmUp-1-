#Given an int n, return True if it is within 10 of 100 or 200.

def near_hundred(n):
  if n in range(90,111):
    return True
  
  elif n in range(190,211):
    return True
  else:return False

near_hundred(93)
near_hundred(90)
near_hundred(89)
