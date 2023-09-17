import random


kids = ["Gabrieli", "Vaxo", "Mariami"]

random.shuffle(kids)

for i in range(3):
    kids[i] += " - does well"


for i in range(len(kids)):
    if kids[i].endswith("i"):
        kids[i] += " - cool"


for kid in kids:
    print(kid)