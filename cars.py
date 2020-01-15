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

