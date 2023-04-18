import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return self._value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("===========================")
        print("Welcome to the Dice Game!")
        print("===========================\n")
        while True:
            self.play_round()

    def play_round(self):
        # Welcome message
        self.print_round_welcome()
        game_over = self.check_game_over()
        if game_over:
            exit()

            # Roll dice Values
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show dice values
        self.show_dice(player_value, computer_value)

        # Compare dice values show winner
        if player_value > computer_value:
            print("you win ༼ つ ◕_◕ ༽つ\n")
            self.update_counter(self._player, self._computer)
            self.show_counter()
        elif player_value < computer_value:
            print("you lose ＞︿＜\n")
            self.update_counter(self._computer, self._player)
            self.show_counter()
        else:
            print("draw ¯\_(ツ)_/¯\n")
            self.show_counter()

    def print_round_welcome(self):
        print("\n-------new round-------")
        input("your turn press any key to roll\n")

    def show_dice(self, player_value, computer_value):
        print(f"\nyou rolled: {player_value}")
        print(f"computer rolled: {computer_value}\n")

    def update_counter(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counter(self):
        print(f"your counter: {self._player.counter}")
        print(f"computer counter: {self._computer.counter}\n")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n===========================")
            print("G A M E   O V E R")
            print("===========================")
            print("The computer won the game. Sorry!")
            print("===========================")

        else:
            print("\n===========================")
            print("You won the game. Congratulations!")
            print("===========================")


player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
my_computer = Player(computer_die, is_computer=True)

game = DiceGame(my_player, my_computer)

game.play()
