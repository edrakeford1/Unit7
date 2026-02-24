"""
Make a list called sandwich_orders and fill it with the name of various sandwiches.
Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders
and print a message for each order, such as "I made you a tuna sandwich". As each sandwich is made, move
it to the list of finished sandwiches. After all of the sandwiches have been made, print a message
listing each sandwich that was made


adding 7-9
No Pastrami
Using the list sandwich_orders from the previous exercise. Make sure the sandwich 'pastrami' appears in
the list at least three times. add code near the beginning of your program to print a message
saying the deli has run out of pastrami, and then use a while loop to remove all occurences
of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches
"""

sandwich_orders = ['reuben', 'grilled cheese', 'pb & j', 'tuna', 'turkey']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I have made you a {sandwich_order} sandwich")
    finished_sandwiches.append(sandwich_order)

# printing the finished sandwiches
print("\nThe sandwiches that have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

