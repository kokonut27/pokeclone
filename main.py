import os
import time
import sys
import getkey
import getpass
import cursor

red = "\033[0;91m"
w = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'
pink = '\033[95m'
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"


# define a clear function
def clear():
  os.system('clear')



# how the map is generated
map = [
  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'e', 'b'],
  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
]

# print the map according where the "shapes" are placed in the map
def print_map():
  global i
  for x in map:
    out = ''
    for i in x:
      if i == 'p':   # p for path
        out += ' '
      elif i == 'b': # b for barrier 
        out += '\t'
      elif i == 'u': # u for user
        out += '8'
      # elif i == 'd': # d for death/deadly :P
      #    out += 'o'
      # elif i == 'e': # e for exit
      #   out +='■'
    print(out)

# hide the cursor so it doesn't go brrr
cursor.hide()

# set the x, y position to (1,1)
y = 1
x = 1

# start the game loop
while True:
  # clear the screen everytime
  os.system('clear')

  # make the user go to the x y cordinates on the map
  map[y][x] = 'u'
  
  # print the map
  print_map()

  try:
    map[y][x] = 'p'
    keyPressed = getkey.getkey()
    
    if keyPressed == 's' and map[y+1][x] != 'b':
      y += 1
    elif keyPressed == 'w' and map[y-1][x] != 'b':
      y -= 1
    elif keyPressed == 'd' and map[y][x+1] != 'b':
      x += 1
    elif keyPressed == 'a' and map[y][x-1] != 'b':
      x -= 1

    # if map[y][x] == 'd':
    #   clear()
    #   print("You Lose") 
    #   break

    # if map[y][x] == 'e':
    #   os.system('clear')
    #   print("Victory")
    #   break
  except:
    pass