import random

pin = ""
while len(pin) != 6:
    pin += str(random.randint(0,9))

print(pin)

