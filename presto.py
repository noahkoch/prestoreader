import os

class Presto(object):
  def capture(self):
    print("Welcome to Presto")
    user_input = None 
    while(user_input != "stop"):
      user_input = input()
      print(f'>>>{user_input}')
      os.system('afplay /System/Library/Sounds/Sosumi.aiff')



Presto().capture()