i = 1
j = 0 

while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
     j = j + i
    i += 1    

print(j)