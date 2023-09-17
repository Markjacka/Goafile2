squad_list = ["Gabriel", "Sandro", "Vano", "Mariam"]

# priveli davaleba
new_list = [name.capitalize() + "supersia" for name in squad_list if name.count("i") > 2]

# meore davaleba
for name in squad_list:
    if len(name) <= 16:
        print(name.upper())

print(new_list)