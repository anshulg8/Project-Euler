target=999
def SumDivisibleBy(n):
  p = int(target / n)
  return int(n*(p*(p+1)) / 2)

print (SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15))
# SumDivisibleBy(3) = (3+6+9+12+...999) = 3(1+2+3+...333)
# SumDivisibleBy(5) = (5+10+15+...200) = 5(1+2+3+...100)
# SumDivisibleBy(15) = (15+30+45+...990) = 15(1+2+3+...66)