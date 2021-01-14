#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, Scissors? (Type Quit to exit) ").lower()
            if move in moves:
                return move
            if move == 'quit':
                print('Bye!')
                exit(0)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.my_move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            if self.my_move == 'rock':
                return 'paper'
            elif self.my_move == 'paper':
                return 'scissors'
            elif self.my_move == 'scissors':
                return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 move: {move1}")
        print(f"Player 2 move: {move2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("**PLAYER 1 WINS THE ROUND**")
        elif beats(move2, move1):
            self.p2_score += 1
            print("**PLAYER 2 WINS THE ROUND**")
        else:
            print("**TIE**")
        print(f"Player 1 score: {self.p1_score}")
        print(f"Player 2 score: {self.p2_score}")

    def play_game(self):
        print("Let's play Rock, Paper, Scissors!\n")
        print("The player that wins by 3 rounds wins the game!\n")
        for round in range(100):
            print(f"Round {round + 1}:")
            self.play_round()
            if self.p1_score > self.p2_score + 2:
                print("**PLAYER 1 WINS THE GAME!**")
                break
            if self.p2_score > self.p1_score + 2:
                print("**PLAYER 2 WINS THE GAME!**")
                break
        print(f"The final score is: ")
        print(f"Player 1: {self.p1_score}")
        print(f"Player 2: {self.p2_score}")
        print("Game over!")


if __name__ == '__main__':
    players = [
        Player(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
