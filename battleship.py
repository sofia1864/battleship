import random
import os
import sys

class Board(object):
  def __init__(self, columns):
    self.alphabet = [ "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    self.columns = columns

  def printboard(self, Player):
    print("Wins: {Player.wins}")
    print("\n  " + " ".join(str(i) for i in self.alphabet))
    for r in range(rowsize):
       print(str(r + 1) + " " + " ".join(str(i) for i in self.columns[r]))
    print()

  def finalisemove(self, player, opponent, cor, symbol):
    rownum = 0
    for row in columns:
      cordindex = -1
      rownum += 1
      for cord in row:
        cordindex += 1
        if cord == cor:
          if opponent.boats.count(cor) > 0:
             columns[rownum[cordindex]] = symbol #only if hit do the symbol
             player.hit += 1
          else:
             columns[rownum[cordindex]] = "M"
             self.misses.append(cor)

  def robotgenerateboats(Robot, Human):
    print("Please stand by; the robot is choosing their boat spots.")
    boats = [ ]
    corswouthuman = [ ]
    for row in board.columns:
      for cor in row:
        corswouthuman.append(cor)
        for cor in Human.boats: #so that no overlap between boats because that would crash game
          if cor == boat:
             corswouthuman.remove(cor)
    number = 1
    otherthree = 0

    while number < 5: 

      number += 1
      otherthree += 1
      if otherthree == 2: #to ensure that two boats taking up three spaces are inputted (because there should be 2 three cor boats)
        number = 2
      orientation = False

      while orientation == False:
        temporaryboatscor = [ random.choice(corswouthuman), random.choice(corswouthuman), random.choice(corswouthuman) ]

        for i in temporaryboatscor:
          checking1.append(i[1])
          options1 = range(1, 10)

        for i in temporaryboatscor:
          checking2.append(i[0])
          options2 = [ ]
          for x in Board.alphabet:
            options2.append(x)

        for i in range(0, len(options1)):
          while i < (len(options1) - 2):
            if checking1 == [ options1[i], options1[i + 1], options1[i + 2]]:
              orientation = True

        for i in range(0, len(options2)):
          while i < (len(options2) - 2):
            if checking2 == [ options2[i], options2[i + 1], options2[i + 2]]:
              orientation = True

      for cor in temporaryboatscor:
         boats.append(cor)
             #checking that meets orientation requirements
    return boats


class Player(object):
  def __init__(self, boats, wins):
    self.boats = boats
    self.wins = wins
    self.hit = 0
    self.lasthit = None #useless for player just need for robot but because they share finalisemove() it's just easier to put it here, won't impact running speed too much
    self.misses = [ ] #same here as lasthit

  def wincondition(self):
    if self.hit == 17:
      print("Congratulations, you have won! Enjoy your hard-earned victory")
      self.wins += 1
      return False
    return True #automatic else because stops once returns something

  def move(self, chosencor, opponent, Board, hitsymbol):
    for row in Board.columns:
      for co_ordinate in row:
        if chosencor == co_ordinate:
          validcor = True
          move(self, opponent, chosencor, hitsymbol)
        else:
          print("Error: You inputted a co-ordinate that is either yours or has already been hit! Kicking you from the game :(")
          sys.exit()


class Robot(Player):
    def __init__(self, boats, wins): 
      super().__init__(boats, wins)

    def nextsquarealgorithim(self, board): 
      availcor = [ ]
      for row in board.columns:
        for cor in row:
          if cor != "M" and cor != "H" and cor != "R":
            for boatcor in self.boats:
              times += 1
              if cor != boatcor and times == 17:
                availcor.append(cor)
      if lasthit.self != None: #hunting algorithim
        lasthit = lasthit.self.split()
        alpha = lasthit[0]
        num = lasthit[1]
        numside = [ ]
        alphaside = [ ]
        if alpha == "A": #accounting for edges so that it won't allow negative indexing or out of range error
           alphaside.append("B")
        elif alpha == "I":
           alphaside.append("H")
        else:
          index = board.alphabet.index(alpha)
          alphaside.append(board.alphabet[index + 1])
          alphaside.append(board.alphabet[index - 1])
        if nums == 9:
          numside.append(8)
        elif num == 1:
          numside.append(2)
        else:
          numside.append(int(numside - 1))
          int(numside + 1)
        for co in availcor:
          if alphaside.count(co[0]) == 0 or alphaside.count(co[1]) in numside:
            availcor.remove(co)
      if len(availcor) == 0: #could come up empty
        newavailcor = [ ]
        for row in board.columns:
          for cor in row:
            if cor != "M" and cor != "H" and cor != "R":
              for boatcor in self.boats:
                times += 1
                if cor != boatcor and times == 17:
                  newavailcor.append(cor)
        return random.choice(newavailcor)

      return random.choice(availcor) #still same because other process just limits down availcor

    def move(self):
      super().move(cor, Human, Board, hitsymbol)

    def wincondition(self):
      if self.hit == 17:
        print("You lost! All of your ships have sunk. Better luck next time!")
      self.wins += 1

def playing(robotwins, humanwins, columns):
    #customizers!
    #setting up game board
    board = [[0] * colsize for i in range(rowsize)]
    gameboard = Board(columns)

    humanboatscor = [ ]
    numberofboats = 1
    otherthree = 0
    number = 1

    while number < 5: 
        number += 1
        print()
        temporaryhumanboatscor = input(f"Where would you like to place your {number} square boat? Input them like so A2, A3, A4 ") #list inside list
        temporaryhumanboatscor = temporaryhumanboatscor.split(", ")
        print()
        orientation = input("Is your boat vertical or horizontal? Please type in lowercase. ")
        checking = [ ]
        options = [ ]
        if orientation == "vertical":
          for i in temporaryhumanboatscor:
            checking.append(i[1])
            options = range(1, 10)
        elif orientation == "horizontal":
          for i in temporaryhumanboatscor:
            checking.append(i[0])
            options = gameboard.alphabet
        else:
          print("Error: Unacceptable orientation, kicking you from the game! <33")
          sys.exit()
        #ensures sequence is in the list (didn't use modulo because can't loop around)
        orientation_confirm = False
        for i in range(0, len(options)):
          while i < (len(options) - 2):
             if checking == [ options[i], options[i + 1], options[i + 2]]:
                orientation_confirm = True
        if orientation_confirm == True:
           print("Error: Boat(s) not placed in the orientation you said it was. Kicking you from the game! ;)")
           sys.exit()
        for cor in temporaryhumanboatscor:
          humanboatscor.append(cor)
        otherthree += 1
        if otherthree == 2: #to ensure that two boats taking up three spaces are inputted (because there should be 2 three cor boats)
            number = 2

    robotboatscor = gameboard.robotgenerateboats(robot, human)
    human = human(humanboatscor, humanwins)
    robot = robot(robotboatscor, robotwins)

    while human.wincondition() and robot.wincondition(): #when neither have won
        humanaim = input("Which square would you like to aim? Please type it like so: A1")
        human.move(humanaim, robot, gameboard, "H") #human's turn
        gameboard.printboard(human)
        robotaim = robot.nextsquarealgorithim(gameboard)
        robot.move(robotaim, human, gameboard, "R") #robot's turn
        gameboard.printboard(human)

    if input("Would you like to play again? ").lower == "yes": #option to play another round, lower is for less chance of malicious input working
      robotwins = robot.wins
      humanwins = human.wins
      playing(robotwins, humanwins) #recursion-type system
    else:
      print("Sad to see you go!")
      sys.exit()

rowsize = 9
colsize = 9

A = [ ]
B = [ ]
C = [ ]
D = [ ]
E = [ ]
F = [ ]
G = [ ]
H = [ ]
I = [ ]
J = [ ]

for i in range(0, 9):
  x = i + 1
  A.append(str("A" + str(x)))
  B.append(str("B" + str(x)))
  C.append(str("C" + str(x)))
  D.append(str("D" + str(x)))
  E.append(str("E" + str(x)))
  F.append(str("F" + str(x)))
  G.append(str("G" + str(x)))
  H.append(str("H" + str(x)))
  I.append(str("I" + str(x)))
  J.append(str("J" + str(x)))

columns = [ A, B, C, D, E, F, G, H, I, J ]

#introduction
print()
print("Welcome to Battleship! I truly hope that you have a fun time playing this game. By the way: Please remember or write down your boat co-ordinates as they will not be shown on the map for extra difficulty! Also, M means miss, H means you hit, and R means robot hit! Quick note: There being two three square boats is not an error, that's just the rules of battleship. Oh, and you're playing in a 9x9 square: Numbers vertical, letters horizontal! ——Sofia, the game's allmightly creator!")
playing(0, 0, columns)
