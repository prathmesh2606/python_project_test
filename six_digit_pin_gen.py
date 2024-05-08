import random

pin = ""
for _ in range(6):
    pin += str(random.randint(0,9))

print(pin)

