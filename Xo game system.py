import os
import random
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class Player:
    def __init__(self):
        self.name=""
        self.symbol=""
        self.score=0
    def choose_name(self):
        while True:
            name=input("Enter the name(letters only): ")
            if name.isalpha():
                self.name=name
                break
            else:
                print("Please enter letters only")
    def choose_symbol(self):
        while True:
            symbol=input("Enter the symbol(X or O): ").upper()
            if symbol in {"X","O"}:
                self.symbol=symbol
                break
            else:
                print("Please enter(X or O):")
    def increase_score(self):
        self.score+=1
class Computer:
    def __init__(self):
        self.name="Computer"
        self.symbol="O"
        self.score=0
    def choose_symbol(self,symbol):
        self.symbol=symbol
class Menu:
    def display_main_menu(self):
        main_menu_text="""Welcome to X-O game🐞
1. Start the game
2. Exit the game
"""
        print(main_menu_text)
        while True:
            choice=int(input("Enter  your choice: "))
            if choice in {1,2}:
                return choice 
            else:
                print("Please enter 1 or 2 ")       
    def display_game_type_menu(self):
        game_type_menu_text="""
1. Two players
2. play with computer 
3. Exit the game"""
        print(game_type_menu_text)
        while True:
            choice=int(input("Enter  your choice: "))
            if choice in {1,2,3}:
                return choice 
            else:
                print("Please enter 1 or 2 ")
    def display_end_menu(self):
        end_menu_text="""
1. Restart the game
2. Exit the game
"""
        print(end_menu_text)
        while True:
            choice=input("Enter  your choice: ")
            if choice in {"1","2"}:
                return choice 
            else:
                print("Please enter 1 or 2: ")  
class Board:
    def __init__(self):
        self.board=[str(x) for x in range(1,10)]
    def display_board(self):
        for i in range(0,10,3):
            print("-"*5)
            print("|".join(self.board[i:i+3]))
    def update_board(self,choice,symbol):
        if self.valid_choice(choice):
            self.board[choice-1]=symbol
            return True
        return False
    def valid_choice(self,choice):
        return self.board[choice-1].isdigit()
    def reset_board(self):
        self.board=[str(x) for x in range(1,10)]
class Game:
    def __init__(self,):
        self.two_players=[Player(),Player()]
        self.computer_and_player=[Player(),Computer()]
        self.board=Board()
        self.mune=Menu()
        self.current_player=0
    def start_game(self):
        choice=self.mune.display_main_menu()
        if choice==1:
            choice=self.mune.display_game_type_menu()
            clear_screen()
            if choice==1:
                self.setup_players(choice)
                self.play_game(choice)
            elif choice==2:
                self.setup_players(choice)
                self.play_game(choice)
            else:
                self.exit_game()
        elif choice==2:
            self.exit_game()
        else:
            print("invalid option ")
    def setup_players(self,choice):
        if choice==1:
            for number,player in enumerate(self.two_players,start=1):
                print(f"Player {number},Enter your details:")
                player.choose_name()
                player.choose_symbol()
                clear_screen()
        elif choice==2:
            self.computer_and_player[0].choose_name()
            self.computer_and_player[0].choose_symbol()
            clear_screen()
    def play_game(self,choice):
        if choice==1:
            self.game_two_players(choice)
        elif choice==2:
            self.game_with_computer(choice)
    def game_two_players(self,choice):
        while True:
            if self.check_wins():
                winner=self.two_players[self.switch_turn()]
                winner.score+=1
                print(f"{winner.name} has won the round ")
                self.print_score(choice)
                choice2=self.mune.display_end_menu()
                if choice2=='1':
                    self.restart_game(choice)
                else:
                    self.print_score(choice)
                    self.print_the_winner(choice)
                    self.exit_game()
            elif self.check_draw():
                choice2=self.mune.display_end_menu()
                if choice2=='1':
                    self.restart_game(choice)
                else:
                    self.print_score(choice)
                    self.print_the_winner(choice)
                    self.exit_game()
            else:
                self.play_turns(choice)
    def game_with_computer(self,choice):
        while True:
            if self.check_wins():
                winner=self.computer_and_player[self.switch_turn()]
                winner.score+=1
                self.board.display_board()
                print(f"{winner.name} has won the round ")
                self.print_score(choice)
                choice2=self.mune.display_end_menu()
                if choice2=='1':
                    self.restart_game(choice)
                else:
                    self.print_score(choice)
                    self.print_the_winner(choice)
                    self.exit_game()
            elif self.check_draw():
                choice2=self.mune.display_end_menu()
                if choice2=='1':
                    self.restart_game(choice)
                else:
                    self.print_score(choice)
                    self.print_the_winner(choice)
                    self.exit_game()
            else:
                self.play_turns(choice)
    def play_turns(self,choice):
        if choice==1:
            player=self.two_players[self.current_player]
            self.board.display_board()
            print(f"{player.name}`s turn({player.symbol})")
            while True:
                try:
                    choice=int(input("Enter your choice (1:9): "))
                    if 1<=choice<=9 and self.board.update_board(choice,player.symbol):
                        clear_screen()
                        break
                    else:
                        print("invalid move")
                except ValueError:
                    print("Please enter 1-9: ")
            self.switch_turn()
            return player
        elif choice==2:
            player = self.computer_and_player[self.current_player]
            self.board.display_board()
            print(f"{player.name}'s turn ({player.symbol})")
            if player.name == "Computer":
                print(f"{player.name}'s turn ({player.symbol})")
                available_moves = [i + 1 for i, cell in enumerate(self.board.board) if cell.isdigit()]
                move = random.choice(available_moves)
                self.board.update_board(move, player.symbol)
                clear_screen()
            else:
                while True:
                    try:
                        move = int(input("Enter your choice (1-9): "))
                        if 1 <= move <= 9 and self.board.update_board(move, player.symbol):
                            clear_screen()
                            break
                        else:
                            print("Invalid move")
                    except ValueError:
                        print("Please enter a number between 1 and 9")
            self.switch_turn()
    def switch_turn(self):
        self.current_player= 1-self.current_player
        return self.current_player
    def print_score(self,choice):
        players = self.two_players if choice == 1 else self.computer_and_player
        print(f"{players[0].name}: {players[0].score}\t{players[1].name}: {players[1].score}")
    def print_the_winner(self,choice):
        players = self.two_players if choice == 1 else self.computer_and_player
        if players[0].score == players[1].score:
            print("The result is a draw!")
        else:
            winner = max(players, key=lambda player: player.score)
            print(f"{winner.name} has won the game")
    def check_draw(self):
        return all(not cell.isdigit()for cell in self.board.board)
    def check_wins(self):
        win_combinations=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]
        for combination in win_combinations:
            if self.board.board[combination[0]]==self.board.board[combination[1]]==self.board.board[combination[2]]:
                return True  
        return False           
    def restart_game(self,choice):
      self.board.reset_board()
      self.current_player=0
      self.play_game(choice)
    def exit_game(self):
        print("Game exited...")
        exit()   
clear_screen()
game=Game()
game.start_game()