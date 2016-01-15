counter = 0
total_sum = 0

while (counter < 999):
  counter += 1
  if (counter % 3 == 0) or (counter % 5 == 0):
    total_sum += counter

print (total_sum)
