print("Hello World")

def p():
  print('---')

# variables
andrew_credit_card = 1237678108769323
glay_credit_card = 4348793847937483
print(andrew_credit_card)
print(glay_credit_card)

# some math
print(3 % 2)
print(10 / 3)

oranges = 5
print("no. of oranges: ")
print(oranges)

x = 4
print(x)
print("---")
print(5 == 5)
print(5 == 4)
print(5 != 4)
print(5 <= 4)
print(5 >= 4)

p()

# if/else statements
print(True)
print(False)

is_john_a_killer = True
is_bob_a_killer = False

if is_john_a_killer == True:
    print("Yes, John is a killer")

# while loops
i = 0
while i < 50:
    print(i)
    i = i + 15

a = 100
while a >= 0:
    if a > 0:
        print(a)
    else:
        print("BOOM!")
    a = a - 1

p()
# for loops
for i in range(101):  # to end at 100, range should be 101
    print(i)

# data types
# integer - 20, 700, 0
# float - 0.245, 12.989
# string - "words"
# list - buckets where we throw stuff like groceries
# ['banana', 'apples','oranges']
# or a list of fighters in a game
# or a list of all the authors if you're making a blogapp
# called an array in Java PL
#tuple - like lists but are harder to change. Think of      this as a ceiled bag
#('banana','apples','oranges')
#dictionary - good for storing 2 pieces of information      together. Like a contact or phonebook
#{"John" : '454-787-5676', "Billy" : '989-576-8888'}
#called a map or a hash in other programming languages

# string + len + looping strings +  string slicing

# len('Hello') in the console

p()


# looping through strings
i = 0
for letter in "Oxydiosis":
    i = i + 1
    print(i)

p()

for i in "TheGodFather":
    print(i)

p()

for letter in "This is awesome":
    print(letter)

p()

for letter in "TheGodFather":
    print("anInstance")

p()

count = 0 #set the count to 0
for letter in "aeroplane": # for every single letter looped through
  count = count + 1 # add 1 to count and loop again
print(count) # then print the result

p()

# lets create a function that counts words o a word

def word_count(word):
  i = 0
  for letter in word:
    i = i + 1
  return i #instead of print

# lets use the function
print(word_count('coxidiosis'))
print(word_count('Helper'))
print(word_count('Python Programming'))

p()

# string indexing
print('Python Programming'[8])
print('Python Programming'[12])
print('Python Programming'[-1])

p()

#search string with string slicing
#print('Python Programming'[start:stop])

print('Python Programming'[9:16])
print('Python Programming'[12:19])
print('Python Programming'[0:15])
print('Python Programming'[0:-1])

p()

#Lists + len + loop + append

groceries = ['banana', 'apples','oranges']
print(groceries)

movies = ['x-men','the god father', 'the queen', 'kings']
print(movies)

p()

print(len(groceries))
print(len(movies))

#you can use len to find out how many blog posts are on the site or how many authors are on the StopIteration

p()
#looping through lists

for movie in movies:
  print(movie)

p()

for item in groceries:
  print(item)

#other uses of for loops: how do you: filter, find the biggest number in a list, how do you find the sum of different numbers exit

#adding more stuff to lists
p()

movies.append('Spiderman')
movies.append('Batman')
print(movies)
print(len(movies))

p()

#you can slice an index list
print(movies[2])
print(movies[5])
print(movies[2:6])
print(movies[0:4])

p()

#summing up numbers in a list
numbers = [23,78,19000,1278,232]

print(numbers)
p()
def sumUp(numbers):
  count = 0
  for number in numbers:
    count = count + number
  return count

print(sumUp(numbers))
numbers.append(10499)

print(sumUp(numbers))
print(numbers)

p()
checks = [284.01,2013.24,400,3600]
print(checks)
print(sumUp(checks))

p()

#find the biggest number in the list
#if you had a leaderboard as you are creating a gaming up, you need to keep track of the one with the highest scores. YOu cannot do this manually. This is how you automate it.

invoices = [34,57,62,20,12,13.99,24.99,99.99]

#let me retry looping through the invoice list
sum = 0
for invoice in invoices:
  sum = sum + invoice
print(sum)
p()

print(sumUp(invoices))
p()

#finding the highest value invoice

def highest(invoices):
  biggest_number = invoices[0]
  for number in invoices:
    if number > biggest_number:
      biggest_number = number
  return biggest_number

print(invoices)
print(highest(invoices))
print(checks)
print(highest(checks))
checks.append(12001.15)
print(checks)
print(highest(checks))
checks.append(120.15)
print(checks)
print(highest(checks))

p()

#finding the smallest value

def smallest(invoices):
  smallest_number = invoices[0]
  for number in invoices:
    if number < smallest_number:
      smallest_number = number
  return smallest_number

print(invoices)
print(smallest(invoices))
p()
print(checks)
print(smallest(checks))


p()

# filter out bad movies
movies = [("Interstellar", 9), ("Iron man", 8.5), ("Superman", 9.3),("Queens", 6.0)] # 3 tuples in a movies list
print(movies)
print(type(movies))
print(len(movies))
print(len(movies[0]))
print(movies[0][0])
print(movies[0][1])
print(movies[1][1])
p()

for movie in movies:
  print(movie)
p()

for title in movies:
  print(title[0])
p()

# now lets filter by rating
for rating in movies:
  if rating[1] > 7:
    print(rating)
p()

def higherRating(movies, rating):
  for movie in movies:
    if movie[1] > rating:
      print(movie)
  p()

higherRating(movies, 9)
higherRating(movies, 7)
higherRating(movies, 0)


# dictionaries hold information that goes in couples like with phonebooks

phonebook = {"John": "444-555-6666", "Peter": "444-534-5556", "Ann": "434-553-6243"}
print(phonebook)
p()

#phonebook['john']

our_movies = {"Tom & Jerry": "9.0", "Spiderman": "8.0", "Batman": "6.0"}
print(our_movies)
p()

authors = {"Rafeh Qazi": ["How to code", "Best PL 2021"], "Andrew Bwogi" : ['How to Cash in JS', 'Introduction to Python PL','ereports.net/dep']}

print(authors)
p()
print(authors['Andrew Bwogi'][2])
p()
print(authors['Rafeh Qazi'])

# Adding values to a dictionary
# keys in dictionaries are always unique
our_movies['Mad Max'] = 3.8 # mad max is the key
our_movies['The Flying House'] = 10

print(our_movies)

p()
# creating a word frequency counter

sentence = 'Hey there what what woop woop woop wap bady booo booo are you doing hey what'
#We use the split() function 

print(sentence.split()) #['Hey', 'there', 'what', 'are', 'you', 'doing', 'hey', 'what']

print(len(sentence.split()))

final_dictionary = {}
for word in sentence.split():
  if word not in final_dictionary:
    final_dictionary[word] = 1
  else:
    final_dictionary[word] = final_dictionary[word] + 1
print(final_dictionary)
p()

#final_dictionary = {'Hey': 1, 'there': 1, 'what': 2, 'are': 1, 'you': 1, 'doing': 1, 'hey': 1}

# let me turn tis into a function 

def wordFreqCounter(sentence):
  final_dictionary = {}
  for word in sentence.split():
    if word not in final_dictionary:
      final_dictionary[word] = 1
    else:
      final_dictionary[word] += 1
  return final_dictionary
  

print(wordFreqCounter(sentence))

p()

newSentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel tincidunt sapien. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel ante ut felis gravida maximus elementum sed arcu. Nulla id tortor diam. Morbi vestibulum congue blandit. Duis commodo in quam eget luctus. Aliquam erat volutpat. Pellentesque varius, sapien at fermentum aliquet, nisl quam dictum erat, ac vulputate mi justo ullamcorper sapien. Nunc fermentum vulputate gravida. Pellentesque lorem nunc, viverra id nibh nec, consectetur tristique nulla. Nam dui orci, tristique in orci bibendum, convallis fermentum libero. Cras leo ante, finibus pellentesque elit et, pulvinar pretium magna. Fusce eleifend elit at tellus auctor, quis sodales sapien porta. Nam dictum lectus et quam luctus facilisis. Nulla in libero sed libero lobortis efficitur id sed velit. Etiam non tristique sapien, a cursus lectus. In tempor fringilla urna, sed placerat ex mollis non. Donec at eleifend est, eget finibus lacus. Donec a magna in metus pulvinar posuere. Ut mollis, diam quis tincidunt tincidunt, tellus est convallis nibh, sed malesuada nulla est quis ipsum. Vestibulum a luctus nunc. In id ex mi. Donec in luctus ante." 

print(wordFreqCounter(newSentence))
p()
