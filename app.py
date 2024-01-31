# a
squares = [ i**2 for i in range(1,6) ]

# squares = []
# for i in range(1,6):
#   squares.append(i**2)

evens = []
for i in range(2,11,2):
  evens.append(i)

people = [
    {"name": "Bob", "age": 35, "city": "Cityville"},
    {"name": "Charlie", "age": 27, "city": "Townsville"},
    {"name": "Diana", "age": 42, "city": "Villagetown"}
]

NAMES = []

for i in people:
  NAME = i["name"].upper()
  NAMES.append(NAME)

print(NAMES)