#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

rnd = 0

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            s = input("Rock, Paper, Scissors? ")
            move = s.lower()
            if move == 'rock' or move == 'paper' or move == 'scissors':
                return move
            if move == 'quit':
                return move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.my_move


class ReflectPlayer(Player):
    def move(self):
        if rnd == 0:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if rnd == 0:
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
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1s = 0
        self.p2s = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 played: {move1}\nPlayer 2 played: {move2}")
        self.p1_returned_move = self.p1.learn(move1, move2)
        self.p2_returned_move = self.p2.learn(move2, move1)
        global rnd
        rnd += 1
        if self.p1_returned_move == "quit" or self.p2_returned_move == "quit":
            return
        elif beats(move1, move2):
            self.p1s += 1
            print("**PLAYER 1 WINS THE ROUND**")
        elif beats(move2, move1):
            self.p2s += 1
            print("**PLAYER 2 WINS THE ROUND**")
        else:
            print("**TIE**")
        print(f"The score is Player 1: {self.p1s}, Player 2: {self.p2s}.\n")

    def play_game(self):
        print("Let's play Rock, Paper, Scissors!\n")
        for round in range(100):
            print(f"Round {round + 1}:")
            self.play_round()
            if self.p1_returned_move == "quit":
                print("**PLAYER QUITS!**")
                break
            if self.p2_returned_move == "quit":
                print("**PLAYER QUITS!**")
                break
            if self.p1s > self.p2s + 2:
                print("**PLAYER 1 WINS THE GAME!**")
                break
            if self.p2s > self.p1s + 2:
                print("**PLAYER 2 WINS THE GAME!**")
                break
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()
