# coding=utf8


"""
          _           _            _                 
    /\   (_)         | |          ( )                
   /  \   _ _ __  ___| | ___ _   _|/ ___             
  / /\ \ | | '_ \/ __| |/ _ \ | | | / __|            
 / ____ \| | | | \__ \ |  __/ |_| | \__ \            
/_/___ \_\_|_| |_|___/_|\___|\__, | |___/            
|  __ \     | | | |           __/ |                  
| |__) |   _| |_| |__   ___  |___/                   
|  ___/ | | | __| '_ \ / _ \| '_ \                   
| |   | |_| | |_| | | | (_) | | | |                  
|_|____\__, |\__|_| |_|\___/|_| |_|                  
 / ____|__/ |      | |                               
| (___ |___/_ _ __ | |_ __ ___  __                   
 \___ \| | | | '_ \| __/ _` \ \/ /                   
 ____) | |_| | | | | || (_| |>  <                    
|_____/ \__, |_| |_|\__\__,_/_/\_\                   
         __/ |                                       
  _____ |___/            _       _               _   
 / ____| |              | |     | |             | |  
| |    | |__   ___  __ _| |_ ___| |__   ___  ___| |_ 
| |    | '_ \ / _ \/ _` | __/ __| '_ \ / _ \/ _ \ __|
| |____| | | |  __/ (_| | |_\__ \ | | |  __/  __/ |_ 
 \_____|_| |_|\___|\__,_|\__|___/_| |_|\___|\___|\__|
                                                      
Find examples below of various abstractions in Python. 
Comments will tell you what's happening. 

Some basic vocab:

defintiion = naming something such as a variable or function
^ also called "declaration" sometimes
invocation = "using" a function/class to do something
expression = sort of like a thought or sentence; will make sense in context
reference  = referring to a variable or function you've already named

Copy stuff from here into a jupyter notebook or a terminal chunk-by-chunk
and watch what happens
"""

### variables: containers for whatever you want

name = "Gazzy Garcia"  # definition  / declaration
age = 20
rap_name = "Lil Pump"  # we'll come back to these
print(name, age, rap_name)  # an expression with references

### data types: there aren't that many
text = "this is some text" # this data type is called a 'string'
number = 124 # just think of numbers as numbers for now
flag = True # `True` or `False` begin with a capital letter. we call them 'booleans'

"""
  _____       _______          _____ _______ _____  _    _  _____ _______ _    _ _____  ______  _____ 
 |  __ \   /\|__   __|/\      / ____|__   __|  __ \| |  | |/ ____|__   __| |  | |  __ \|  ____|/ ____|
 | |  | | /  \  | |  /  \    | (___    | |  | |__) | |  | | |       | |  | |  | | |__) | |__  | (___  
 | |  | |/ /\ \ | | / /\ \    \___ \   | |  |  _  /| |  | | |       | |  | |  | |  _  /|  __|  \___ \ 
 | |__| / ____ \| |/ ____ \   ____) |  | |  | | \ \| |__| | |____   | |  | |__| | | \ \| |____ ____) |
 |_____/_/    \_\_/_/    \_\ |_____/   |_|  |_|  \_\\____/ \_____|  |_|   \____/|_|  \_\______|_____/  

 Data structures are everything and everywhere. Grasping these and knowing them when you see them
 will vastly improve your experience with Python and technology in general.

 Everything you see below is using "literal" data types.
 [] is a "list literal"
 {} is a "dict literal"
 () is a "tuple literal"
 etc.
"""

# list: holds anything you want in any order
numbers = [1, 2, 3]  # definition / declaration
numbers

numbers[0]  # use 'indices' to access stuff. first element is 0
numbers[-1]  # the last element is -1
numbers[0:1]  # 'slicing' will get the elements within that range

# tuple: "list-like". does similar stuff to lists, almost interchangeable.
# only included here to introduce you to the idea of things being 'list-like'
random_stuff = ("dogs", 66, numbers)
# print(random_stuff)  # note the list inside the tuple

# dictionary: look up values of any kind with keys. best data structure!
webster = {
    "petrichor": "the smell of freshly fallen rain",
    "verdant": "having green coloration",
    "sufjan": "a sad alien who loves god.",
}

webster["petrichor"] # keys are always strings

# use old references to build new structures
# such as an abstraction of a soundcloud rapper using a dict
lil_pump = {"name": name, "age": age, "rap_name": rap_name}

# mash random stuff together into complex structures
mish_mash = [webster, random_stuff, numbers, lil_pump]

from pprint import pprint # it stands for 'pretty print'. issa module. we'll cover more on modules later

pprint(lil_pump)
pprint(mish_mash)

# remember when i said  a tuple is 'list-like'? 
# tip: tables and data frames are kinda like lists of dicts

soundcloud_rappers = [
    lil_pump,
    {"name": "Daniel Hernandez", "age": 22, "rap_name": "6ix9ine"}, # dicts are rows
    {"name": "Symere Woods", "age": 24, "rap_name": "Lil Uzi Vert"}, # their keys are columns
    {"name": "Jarad Higgins", "age": 19, "rap_name": "Juice Wrld"}, # u feel me?
]

pprint(soundcloud_rappers)

"""
   _      ____   _____ _____ _____         _                                         
 | |    / __ \ / ____|_   _/ ____|       | |                                        
 | |   | |  | | |  __  | || |        __ _| | ____ _                                 
 | |   | |  | | | |_ | | || |       / _` | |/ / _` |                                
 | |___| |__| | |__| |_| || |____  | (_| |   < (_| |                                
 |______\____/ \_____|_____\_____|  \__,_|_|\_\__,_|                                
   _____ ____  _   _ _______ _____   ____  _        ______ _      ______          __
  / ____/ __ \| \ | |__   __|  __ \ / __ \| |      |  ____| |    / __ \ \        / /
 | |   | |  | |  \| |  | |  | |__) | |  | | |      | |__  | |   | |  | \ \  /\  / / 
 | |   | |  | | . ` |  | |  |  _  /| |  | | |      |  __| | |   | |  | |\ \/  \/ /  
 | |___| |__| | |\  |  | |  | | \ \| |__| | |____  | |    | |___| |__| | \  /\  /   
  \_____\____/|_| \_|  |_|  |_|  \_\\____/|______| |_|    |______\____/   \/  \/    

Your code needs to be able to handle different data differently. 
We write our code so that it can act differently for different situations
using logic that resembles the way we think irl.

Comparing if things are equal (like in a where clause in SQL) 
is done with a double equals sign. != or "bang equals" is the opposite.

55 == 55 returns True
55 != 55 returns False
55 == 54 returns False
True != False returns True

There's also:
greater than     >
less than        >
greater or equal >=
less or equal    <=
"""

best_rapper = "Kendrick"
now_playing = ""  # change this value and see how the output of the expression below changes

if now_playing == best_rapper:
    print( "Nice. You have good taste.")
else:
    print( "You should probably be listening to Kendrick.")

"""
           _____  ____ _____ _______ _____            _______     __                    
     /\   |  __ \|  _ \_   _|__   __|  __ \     /\   |  __ \ \   / /                    
    /  \  | |__) | |_) || |    | |  | |__) |   /  \  | |__) \ \_/ /                     
   / /\ \ |  _  /|  _ < | |    | |  |  _  /   / /\ \ |  _  / \   /                      
  / ____ \| | \ \| |_) || |_   | |  | | \ \  / ____ \| | \ \  | |                       
 /_/   _\_\_|__\_\____/_____|  |_|__|_|__\_\/_/____\_\_|__\_\ |_|______ _____           
 | |  | |/ ____|  ____|  __ \   |  __ \|  ____|  ____|_   _| \ | |  ____|  __ \          
 | |  | | (___ | |__  | |__) |  | |  | | |__  | |__    | | |  \| | |__  | |  | |         
 | |  | |\___ \|  __| |  _  /   | |  | |  __| |  __|   | | | . ` |  __| | |  | |         
 | |__| |____) | |____| | \ \   | |__| | |____| |     _| |_| |\  | |____| |__| |         
  \____/|_____/|______|_|__\_\  |_____/|______|_| ___|_____|_|_\_|______|_____/ _  _____ 
     /\   |  _ \ / ____|__   __|  __ \     /\   / ____|__   __|_   _/ __ \| \ | |/ ____|
    /  \  | |_) | (___    | |  | |__) |   /  \ | |       | |    | || |  | |  \| | (___  
   / /\ \ |  _ < \___ \   | |  |  _  /   / /\ \| |       | |    | || |  | | . ` |\___ \ 
  / ____ \| |_) |____) |  | |  | | \ \  / ____ \ |____   | |   _| || |__| | |\  |____) |
 /_/_  _\_\____/|_____/   |_|  |_|  \_\/_/    \_\_____|  |_|  |_____\____/|_| \_|_____/ 
  / / | | | |                                | |     | |        / _|/ _| \ \            
 | |  | |_| |__   ___    __ _  ___   ___   __| |  ___| |_ _   _| |_| |_   | |           
 | |  | __| '_ \ / _ \  / _` |/ _ \ / _ \ / _` | / __| __| | | |  _|  _|  | |           
 | |  | |_| | | |  __/ | (_| | (_) | (_) | (_| | \__ \ |_| |_| | | | |    | |           
 | |   \__|_| |_|\___|  \__, |\___/ \___/ \__,_| |___/\__|\__,_|_| |_|    | |           
  \_\                    __/ |                                           /_/            
                        |___/                                                           

This is that good good. Functions, modules, (and occasionally classes) are where
the full power of everything above gets rolled together to accomplish tasks of all varieties.
"""


"""
Functions are declared with the keyword `def`
Functions take "arguments" which are just inputs
Functions should "return" something _always_. Your functions sucks if it doesn't.

Using a function is called "invocation" or "calling"

def function(args):
    return stuff

Give your functions names that describe what they do. Shorter is *not* better when it comes 
to names. If it's a lot to explain, put a damn comment.
"""


# functions can do simple stuff
def add_one(x):
    return x + 1

add_one(5)


# functions can build data structures
def build_rapper(name, age, rap_name):
    print("You've made a rapper named " + rap_name + ".")
    return {"name": name, "age": age, "rap_name": rap_name}

# note how you specify keywords in your arguments. these are called "kwargs"
build_rapper(name="Sean Carter", age="OOOOOLD", rap_name="Jay Z" )


# functions are "first class citizens" meaning they can be used pretty much everywhere
build_rapper(
    name="Chancelor Bennett", 
    age=add_one(24),  # function call in a function call!
    rap_name="Chance the Rapper")

# functions are where we make use of logic
def make_me_act_a_fool(location):
    if location == "up in here":
        return "Y'all gon' make me act a fool up in here!"
    elif len(location) != 0: 
        return "Y'all gon' make me act a fool up in " + location + "!"
    else:
        return "Yall gon' make me act a fool...somewhere..."

"""
This section on modules is a very high level look at what they are.
You won't need to know how to write them to use python for analytics,
but knowing one when you see it will make your work easier to think about.

Any time you use the keyword `import` you're interacting with a module.
This file is technically a module. Any time you use a . (dot) you are accessing something in a module.
It could be a function or a variable or even another module. Sky's the limit!

You can run `import cheatsheet` in your notebook/terminal and then be able to use
any of the things defined here. (Kind of useless, but illustrative.)

Try running `cheatsheet.lil_pump` or `cheatsheet.make_me_act_a_fool("up in here")`
"""

import random # used for generating random numbers
random.randint(0,1) # dot notation lets us access the parts of a module

"""
Only gonna make one brief note on classes.

Classes are packages of functionality like modules, 
but rather than being defined as files, they're written out in scripts the way functions are.

You will use a lot of dots ( . ) when using pandas. This is because pandas is a module full of classes.
You will not need to implement classes of your own in the near future, but it's informative to see
how they work since you will make use of them very often.
"""

class Dog: # declared with the keyword `class`, must be named in TitleCase
    
    # this is a special thing we have to do to classes to intialize them
    # here, we set the variables that will describe the dog. we call these "fields"
    # users never touch __init__ directly, but we'll see where it comes into play soon
    def __init__(self, name=None, bark_sound=None, needs_food=None, last_meal=None):
        # ^ everything arg needs to be a kwarg, and all of them need sensible defaults
        self.name = name
        self.bark_sound = bark_sound
        self.needs_food = needs_food
        self.last_meal = last_meal

    # this function (or, more accurately, this "method") sets a bark for our dog
    # when it's inside a class, a function is referred to as a "method"
    def set_bark(self, bark_sound): 
        # the self ^ paramer is weird, we declare it but don't actually call these methods with it.
        # don't think about it too much.
        self.bark_sound = bark_sound
        return self # a good class returns itself when you set something, see why soon.

    # this will return the bark we've given our dog, or nothing if we didn't give it one
    def bark(self):
        # ^ this is the equivalent of a function that takes 0 args
        return self.bark_sound

    # this is for naming the dog
    def give_name(self, name):
        self.name = name
        return self
    
    # take good care of this dog.
    def feed(self, food):
        if self.needs_food == False:
            print("Sorry, I'm not hungry.")
            return self
        else:
            self.needs_food = False
            self.last_meal = food
            print( "Thx 4 giving me that " + food)
            return self
        
# now that we have a class, let's demonstrate a few things you *will* encounter

# if you're at a terminal run `from cheatsheet import Dog` rather than copy/pasting

# initialization aka instantiation looks a lot like calling a function
my_dog = Dog() # we now have an instance of the dog class


my_dog.bark() # returns None cuz we never set a bark sound
# note how we use dots to access dog functionality -- just like modules!
my_dog.set_bark("YEEHAW")
my_dog.bark() # we changed our dog's bark! that's weird, huh

# lets remake that dog, but we'll use that weird __init__ thing this time
# we use it indirectly by passing args directly into the class instance
my_dog = Dog(name="Woofer", bark_sound="yip yip yip")
my_dog.name # accessing a field directly
my_dog.bark() # using a class method

# method chaning is a way to do a bunch of stuff to a class instance at once
# let's overwrite our dog's features with new stuff
my_dog = (
    my_dog
    .set_bark("achoO!") # weird dog
    .give_name("Snuggles")
    .feed("asparagus") # don't do this irl
)

# all three of those methods ^ returned the dog itself, which allowed us to chain like that
# you will see a _ton_ of this in Pandas, just you wait.

# see how things have changed??
my_dog.bark()
my_dog.name 
my_dog.last_meal
