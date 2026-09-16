#Get A Key
#you can access the values in it by providing the key:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#La linea anterior crea el diccionario "Building_heights" con 6 elementos, sus llaves representas sus alturas en metros
print(building_heights["Burj Khalifa"]) # Imprime la llave del elemento "Burj Khalifa"
print(building_heights["Ping An"]) # Imprime la llave del elemento "Ping An"

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
#La linea anterior crea el diccionario "zodiac_elements" con 4 conjuntos; water,fire, earth y air, cada uno con 3 elementos. 
print(zodiac_elements["earth"])#Imprime los elementos del conjunto earth perteneciente al diccionario zodiac_elements
print(zodiac_elements["fire"])#Imprime los elementos del conjunto fire perteneciente al diccionario zodiac_elements

# Get an Invalid Key

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#La linea anterior crea el diccionario "Building_heights" con 6 elementos, sus llaves representas sus alturas en metros
#print(building_heights["Landmark 81"]) #Intenta impirmir el elemento "Landmark 81", pero al no existir en el diccionario, da un error de llave

#One way to avoid this error is to first check if the key exists in the dictionary:
key_to_check = "Landmark 81" #comprueba si la llave existe en el diccionario

if key_to_check in building_heights:
    print(building_heights["Landmark 81"]) #si existe la llave "key_to_check" en "builing_heights", se imprimirá 

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
#La linea anterior crea el diccionario "zodiac_elements" con 4 conjuntos; water,fire, earth y air, cada uno con 3 elementos.
zodiac_elements["energy"] = "Not a Zodiac element" #Añade la llave "energy" cómo "not a zodiac element" adentro del diccionario

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"]) #Si energy hace parte de zodiac_elements, se va a imprimir "Not a zodiac element"

#Safely Get a Key
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#La linea anterior crea el diccionario "Building_heights" con 6 elementos, sus llaves representas sus alturas en metros
#this line will return 632:
building_heights.get("Shanghai Tower") #Obtiene de manera segura la llave de "Shangai Tower"

#this line will return None:
building_heights.get("My House") #Obtiene de manera segura la llave de "My house"

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#La anterior linea define el diccionario user_ids con 5 elementos y sus respectivas llaves
user_ids.get("teraCoder") #Guarda el valor de la llave con nombre "teraCoder"

if user_ids.get("teraCoder") == None:
    tc_id = 1000    #Si el valor de TeraCoder no aparece en el diccionario, se define tc_id con un valor constante de 1000
else: 
    tc_id = user_ids.get("teraCoder") #Si el valor de TeraCoder aparece en el diccionario, se guarda tc_id cómo el valor definido en el diccionario  

print(tc_id) #Imprime el valor de tc_id

if user_ids.get("superStackSmash") == None:
      stack_id = 100000 #Si la llave "superStackSmash" no está en el diccionario, se define stack_id con un valor de 100000

print(stack_id) #Imprime el valor de stack_id

#Delete a Key
#.pop() works to delete items from a dictionary, when you know the key value.
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
#La anterior linea define el diccionario raffle con 5 elementos númericos y sus respectivas llaves
print(raffle.pop(320291, "No Prize")) # Imprime "Gift Basket", que fue el elemento borrado
print(raffle) #Imprime todo el diccionario menos la llave eliminada 
print(raffle.pop(100000, "No Prize"))# Imprime "No Prize" porque nigún elemento tiene esta llave
print(raffle) ##Imprime todo el diccionario menos la llave eliminada
print(raffle.pop(872921, "No Prize")) # Imprime "Concert Tickets", que fue el elemento borrado
print(raffle)# Imprime todos los elementos menos los 2 eliminados 

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
#La anterior linea define el diccionario avaliable_items con 6 elementos y sus respectivas llaves
health_points = 20 #define la variable health_points

health_points += available_items.pop("stamina grains", 0) #suma el valor de la llave "stamina grains" a "health_points" 
health_points += available_items.pop("power stew", 0) #suma el valor de la llave "power stew" a "health_points"
health_points += available_items.pop("mystic bread", 0) #suma el valor de la llave "mystic bread" a "health_points"

print(available_items) #Imprime el diccionario "Avalible Items" sin los 2 items que han sido borrados
print(health_points) #Imprime la suma entre healt_points con los valores borrados del diccionario

#Get All Keys
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#La linea anterior crea el diccionario "test_scores" con 6 conjuntos; grace,Jeffrey,Sylvia,Pedro,Martin y dina, cada uno con 3 elementos.
print(list(test_scores)) #Habilita hacer listas con el diccionario "test_scores"

for student in test_scores.keys():
  print(student) #Hace e imprime una lista de todas las llaves del diccionario  "test_scores"

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#La anterior linea define el diccionario user_ids con 5 elementos y sus respectivas llaves
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
#La anterior linea define el diccionario user num_exercises con 7 elementos y sus respectivas llaves
users = user_ids.keys() #Define users cómo la lista de llaves del diccionario user_ids
lessons = num_exercises.keys() #Define lessons cómo la lista de llaves del diccionario num_exersices

print(users) #imprime users
print(lessons) #imprime lessons

#Get All Values
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#La linea anterior crea el diccionario "test_scores" con 6 conjuntos; grace,Jeffrey,Sylvia,Pedro,Martin y dina, cada uno con 3 elementos.
for score_list in test_scores.values():
  print(score_list) #Hace e imprime una lista de los valores en el diccionario por cada grupo, siendo 6 listas en total
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
#La anterior linea define el diccionario user num_exercises con 7 elementos y sus respectivas llaves
total_exercises = 0 #define total_exercises

for exercises in num_exercises.values():
   total_exercises += exercises #suma los valores de cada llave de num_exercises en la variable "total_exercises"
print(total_exercises) #imprime el resultado de total_exercises

#Get All Items
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
#La anterior linea define el diccionario user biggest_brands con 5 elementos y sus respectivas llaves
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ") #Hace una lista con todos los elementos del diccionario e imprime las llaves en company y los valores en value

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
#La anterior linea define el diccionario user biggest_brands con 6 elementos y sus respectivas llaves
for occupation, percentage in pct_women_in_occupation.items():
   print("Women make up " + str(percentage) + " percent of " + occupation + "s.")  #Hace una lista con todos los elementos del diccionario e imprime las llaves en occupation y los valores en percentage
