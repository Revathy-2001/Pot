
n = int(input())
lst = []
for i in range(n):
  v = int(input())
  if(v >= 10 and v <= 10000):
    lst.append(v)
if(len(lst) == n):
  store = []
  for i in lst: 
    store.append(str(i))
  tot = 0
  for i in store:
    s = len(i)
    power = i[-1]
    num = i[:(s-1)]
    power = int(power)
    num = int(num)
    temp = pow(num,power)
    tot = tot + temp;
  print(tot)
  
