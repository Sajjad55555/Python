# Write a separate program to accomplish each of these exercises. Save each program with a
# filename that follows standard Python conventions, using lowercase 
# letters and underscores, such as simple_message.py and simple_messages.py.
# 2-1. Simple Message: Assign a message to a variable, and then print that 
# message.
simple_message:str = "heloo world"
print(simple_message)
# 2-2. Simple Messages: Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new 
# message.
new_message = simple_message
print(new_message)
#  Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?
name:str="sajjad haider"
messagae:str=f'''"hello {name}, would you like to learn some python today'''
print(messagae)
# Name Cases: Use a variable to represent a person’s name, and then print 
#that person’s name in lowercase, uppercase, and title case
print(name.lower())
print(name.title())
print(name.upper())
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:Albert Einstein once said, “A person who never made a
#  mistake never tried anything new.
quote:str='"A person who never made a mistake never tried anything new."'
print("Albert Einstein once said," + quote)
# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous 
# person’s name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message.
famous_person:str="Albert Einstein"
print(f'''{famous_person} once said,{quote} ''')
# 2-7. Stripping Names: Use a variable to represent a person’s name, and 
# include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().
# Defining the name variable with whitespaces
name = "\t  John Doe \t"
print(name)
print( name.lstrip())
print( name.rstrip())
print( name.strip())
# 2-8. File Extensions: Python has a removesuffix() method that works exactly 
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called 
# filename. Then use the removesuffix() method to display the filename without 
# the file extension, like some file browsers do
pthon_extention:str = 'python_notes.txt'
print(pthon_extention.removesuffix('.txt'))
# 2-9. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your operations 
# in print() calls to see the results. You should create four lines that look like this:
# print(5+3)
# Your output should be four lines, with the number 8 appearing once on 
# each line.
print(6 + 2)
print(10 - 2)
print(4 * 2)
print(int(16 / 2))
# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, 
# using that variable
favorite_number = 7
print("My favorite number is:", favorite_number)
# 2-11. Adding Comments: Choose two of the programs you’ve written, and 
# add at least one comment to each. If you don’t have anything specific to write 
# because your programs are too simple at this point, just add your name and the 
# current date at the top of each program file. Then write one sentence describing 
# what the program does
comments:str="comments already in my exercise"

# 2-12. Zen of Python: Enter import this into a Python terminal session and skim 
# through the additional principles


