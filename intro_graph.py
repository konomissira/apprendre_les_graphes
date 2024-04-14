print("******************************************")
print("******************************************")
person = {}

person["Rashford"] = [26, 185]
person["Dembele"] = [26, 178]

print(person)
print("******************************************")

general = {}
general["Robert"] = ["William", "Marta", "John"]
general["William"] = ["Amy"]
general["Marta"] = []
general["John"] = ["Alison", "Jack"]

print(general)
print(general["John"])
print("******************************************")

cities = {}

cities["London"] = {"Reading":70, "Brighton":88, "Oxford":100}
cities["Reading"] = {"London":70, "Brighton":138, "Oxford":42}
cities["Brighton"] = {"London":88, "Reading":138, "Oxford":177}
cities["Oxford"] = {"London":100, "Reading":42, "Brighton":177}

print("The distance between London and Oxford is: ", cities["London"]["Oxford"], " Km")

print("******************************************")

cities_matrice = [[0, 70, 88, 100],
                    [70, 0, 138, 42],
                    [88, 138, 0, 177],
                    [100, 42, 177, 0]]

print("The distance betwen London and Reading is: ",cities_matrice[0][1], " km.")
print("The distance betwen London and Oxford is: ",cities_matrice[0][3], " km.")