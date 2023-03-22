#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
exercise1_string = "The girl in red"
exercise1_number = 32
exercise1_list = [32, 'girl', True]
exercise1_boolean = True

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
new_exercise2_string = exercise1_string[:3]
print(new_exercise2_string)

#Exercise 3: Use an index to grab the first element from your list.
another_exercise2_string = exercise1_string[0]
print(another_exercise2_string)

#Exercise 4: Create a new number variable that adds 10 to your original number.
exercise4_number = exercise1_number + 10
print(exercise4_number)

#Exercise 5: Use an index to get the last element in your list.
other_exercise2_string = exercise1_string[-1]
print(other_exercise2_string)

#Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')
print(list_of_names)

'''Exercise 7: Get the first word from your string using indexes. 
Use the upper function to transform the letters into uppercase. 
Create a new string that takes the uppercase word and the rest of the original string.'''
exercise7_string = exercise1_string.upper()[:3] + exercise1_string[3:]
print(exercise7_string )


#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
exercise8 = f'The girl in red is {exercise1_number} m far'
print(exercise8)

#Exercise 9: Print “hello world”.
exercise9 = "hello wold"
print(exercise9)