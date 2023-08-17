#tic tac toe game


#board
board=["-","-","-","-","-","-","-","-","-"]

game_still_going=True

#who won or tie
winner=None

#whose turn
current_player="X"


#board display
def display() :
   print(board[0] +" |"+board[1] + " |"+  board[2])
   print(board[3] +" |"+board[4]+ " |" + board[5])
   print(board[6] +" |"+board[7] +" |"+ board[8])


  
#writingg a function that drives the game
  
def play_game():
  
  # 1.displaying the board
  display()
  
  # game logic looping untill the game is Over
  while game_still_going:
    
   #handle a single turn 
    handle_turn(current_player)

    #check if the game has ended
    check_if_game_over()

    #Flip to the other player
    filp_player()
    
  # if game has ended out of while loop now->
  if winner=="X" or winner== "O":
    print(winner+" won")
  elif winner==None:
    print("Tie")
    
def handle_turn(player):
  print(player,"s turn ")
  position =(input("choose a position from 1 to 9: "))
  valid =False
  while not valid:
   while position  not in ["1","2","3","4","5","6","7","8","9"]:
    position =input("invalid input ,choose a position from 1 to 9: ")
    
   position=int(position)-1
   if board[position]=="-":
    valid=True
   else:
    print("you cant go their ,go again")
    
  board[position] = player
    
  display()


def check_if_game_over():
  check_for_winner()
  check_tie()


def check_for_winner():
  global winner
  row_winner= check_row()
  colomun_winner= check_coloumns()
  diagonal_winner=check_diagonals()

  if row_winner:
    winner=row_winner
  elif colomun_winner:
    winner=colomun_winner
  elif diagonal_winner:
    winner =diagonal_winner
  return

def check_row():
  global game_still_going
  r1=  board[0]==board[1]==board[2]!="-" #if satisfied r1 will be true
  r2=  board[3]==board[4]==board[5]!="-"
  r3=  board[6]==board[7]==board[8]!="-"

  if r1 or r2 or r3:
    game_still_going=False
  if r1:
    return board[0]
  elif r2:
    return board[3]
  elif r3:
    return board[6]
    
  
  return 
def check_coloumns():
   global game_still_going
   c1=  board[0]==board[3]==board[6]!="-"  #if satisfied c1 will be true
   c2=  board[1]==board[4]==board[7]!="-"
   c3=  board[2]==board[5]==board[8]!="-"

   if c1 or c2 or c3:
    game_still_going=False
   if c1:
    return board[0]
   elif c2:
    return board[1]
   elif c3:
    return board[2]
    

   return


def check_diagonals():
   global game_still_going
   d1=  board[0]==board[4]==board[8]!="-"  #if satisfied c1 will be true
   d2=  board[2]==board[4]==board[6]!="-"
   if d1 or d2 :
    game_still_going=False
   if d1:
    return board[0]
   elif d2:
    return board[2]
   return
  
  
def check_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False
  
  return

def filp_player():
  global current_player
  if current_player=="X":
   current_player="O"
  else :
   current_player="X"
  return



    
play_game()


  
  


#board
#board display
#play game 
#handle turn
#check win
  #check row 
  #check collumns 
  #check diagonlas
#check tie
#flip player
