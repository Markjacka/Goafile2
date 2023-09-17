import random

crew_leaders = ['kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze', 'aruda']

for _ in range(3):  # 3 ჯერ გამოიყენეთ
    if crew_leaders:  # თუ წევრების სია ცარიელი არ არის
        winner = random.choice(crew_leaders)
        print('Winner is', winner)
        crew_leaders.remove(winner)  # წევრის წაშლა წევრების სიიდან
    else:
        print("No more crew leaders left.")
