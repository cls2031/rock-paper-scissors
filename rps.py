#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer:
    def move(self):
        return random.choice(moves)
    
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

class HumanPlayer:
    def move(self):
        while True:
            s = input("Rock, Paper, Scissors? ")
            move = s.lower()
            if move == 'rock' or move == 'paper' or move == 'scissors':
                return move
    
    def learn(self, my_move, their_move):
        pass
 
class ReflectPlayer:
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return their_move
        
class CyclePlayer:
    def move(self):
        return random.choice(moves)
    
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        if my_move == 'rock':
            return 'paper'
        elif my_move == 'paper':
            return 'scissors'
        elif my_move == 'scissors':
            return 'rock'

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0
        self.turn = 0
      
    def play_round(self):
        if self.turn == 0:
            move1 = self.p1.move()
            move2 = self.p2.move() 
            print(f"Opponent played: {move1}\nYou played: {move2}")
            self.returned_move = self.p1.learn(move1, move2)
            # self.p2.learn(move2, move1)
            self.turn += 1
        else:
            move1 = self.returned_move
            move2 = self.p2.move()
            print(f"Opponent played: {move1}\nYou played: {move2}")
            self.returned_move = self.p1.learn(move1, move2)
            # self.p2.learn(move2, move1)
            self.turn += 1
        if beats(move1, move2):
            self.p1score += 1
            print("**PLAYER 1 WINS**")
        elif beats(move2, move1):
            self.p2score += 1
            print("**PLAYER 2 WINS**")
        else:
            print("**TIE**")
        print(f"The score is Player 1: {self.p1score}, Player 2: {self.p2score}.\n")


    def play_game(self):
        print("Let's play Rock, Paper, Scissors!\n")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
