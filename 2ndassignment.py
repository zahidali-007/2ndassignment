#  ---------------------------->>> Numbers <<<----------------------------
# Random Number
import random
print(random.randrange(1, 10))

# There are three types of Numbers in Python:
# int
# float
# complex
a = 5    # int
b = 4.8  # float
c = "WizInsights"   # String
d = 5j   # complex
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#  ---------------------------->>> Tuples <<<----------------------------
std_name = ("Zahid", "Ali", "Farhan", "Tasneem", "Gul")
Fruits = ("orange", "banana", "apples", "grapes")
print(std_name)
print(type(std_name))
print(len(std_name))
print(std_name[1])
print(std_name[-2])
print(std_name[2:4])
b = list(std_name)
b[2:4] = "pea", "cabbage"
std_name = tuple(b)
print(std_name)
b.append("tomato")
std_name = tuple(b)
print(std_name)
b.remove("cabbage")
std_name = tuple(b)
print(std_name)
# unpacking of tuple
print("onion")
print("potato")
print("tomato")
print("pepper")
print("carrot")
# Joining and multiplying of tuples
print(std_name + Fruits)
print(std_name*3)
# delete std_name -> print(std_name) tuple is deletd due to it causes an error.

#  ---------------------------->>> Lists <<<----------------------------
my_list = [13, 15, 2, 5, 7, "RYK", "Lahore", "ICT", "KPK", "Sindh"]
a_list = [True, False, False, True]
print(my_list)
# Check length of list
print(len(my_list))
# Access list's items
print(my_list[:5])
print(my_list[3:])
print(my_list[4:9])
print(my_list[-6:-3])
# Sort list
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)
# Add items
my_list.append("Peshawar")
print(my_list)
my_list.insert(3, "Karachi")
print(my_list)
my_list.extend(a_list)
print(my_list)
# Joining of lists
print(a_list + my_list)
my_list.extend(a_list)
print(my_list)
# Remove item from list
my_list.remove("KPK")
print(my_list)
del my_list[4]
print(my_list)
# pop method also used to remove a specific item from list.
my_list.pop()
print(my_list)
# Check index
print(my_list.index("Sindh"))
# Change item of list
my_list[1:3] = ["SDK", "FSD"]
print(my_list)
# Check type of list
print(type(my_list))
# Copy list
my_list = a_list.copy()
print(my_list)
my_list = list(a_list)
print(my_list)

#  ---------------------------->>> Dictionary <<<----------------------------

country_code = {"pakistan": 250, "india": 300,
                "USA": 700, "UK": 500, "Europe": 90}
print(country_code["USA"])
# Check keys of dictionary
print(country_code.keys())
# Check type of dictionary
print(type(country_code))
# Change dictionary
country_code["USA"] = 10
print(country_code)
# Update dictionary
country_code.update({"UK": 15})
print(country_code)
# delelte method remove a specific item and also removes the whole dictionary this will cause an error
del (country_code["india"])
print(country_code)
country_code.pop("USA")
print(country_code)
country_code.popitem()
print(country_code)
# remove items from dictionary
country_code.clear()
print(country_code)
