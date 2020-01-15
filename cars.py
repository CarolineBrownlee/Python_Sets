# A set is a collection of things, like a list, but the collection is both unordered, and contains no duplicate elements. Developers use sets to easily filter down other collections to unique elements, and to see if two, or more, collections share any similar items.

# You can create a set in one of two ways.

# 1. Using set() to create a set
# languages = set()

# 2. Using curly braces allows you to initialize the set with values
# languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }

# SHOWROOM AND JUNKYARD PRACTICE EXERCISE:

# 1. Create an empty set named showroom.
showroom = set()

# 2. Add four of your favorite car model names to the set.
showroom.add("Land Rover")
showroom.add("Pilot")
showroom.add("Explorer")
showroom.add("Outback")

# 3. Print the length of your set.
print(showroom)

# 4. Pick one of the items in your show room and add it to the set again.
showroom.add("Land Rover")

# 5. Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

# 6. Using update(), add two more car models to your showroom with another set.
second_showroom = set()
second_showroom.add("Jetta")
second_showroom.add("Range Rover")
print(second_showroom)
showroom.update(second_showroom)
print(showroom)

# 7. You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Range Rover")
print(showroom)

# Acquiring more cars:
# 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = set()
junkyard.add("Leaf")
junkyard.add("Durango")
junkyard.add("Jetta")
junkyard.add("Pilot")
print(junkyard)

# 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
intersection = showroom.intersection(junkyard)
print(intersection)

# 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
union = showroom.union(junkyard)
print(union)

# 4. Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
union.discard("Leaf")
union.discard("Durango")
print(union)