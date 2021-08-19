import random        
ring = random.randint(1,18)
print(ring)
for i in range(1,19):
    if i == ring:
        print(i)
        break
    print(i)