def result(limit):
  sum = 0
  a = 1
  b = 1
  c = a + b
  while (c < limit):
    sum += c # Every 3rd no is even number
    a = b + c
    b = c + a
    c = a + b
  return sum

limit = 4000000
print (result(limit))