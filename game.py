#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:04:39 2022

@author: amolbhagavathi
"""

    
class tic_tac_toe:
    def __init__(self):
        self.board = [" " for i in range(9)]
        # self.board is [" ", " "," ", " ", " ", " ", " ", " ", " "]
        self.winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print ("| "+" | ".join(row)+" |")
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        #print (number_board)
        for row in number_board:
            print ("| "+" | ".join(row)+" |")
            
    def available_moves(self):
        moves = []
        for (index,spot) in enumerate(self.board):
            if spot == " ":
                moves.append(index)
                #appends index of spot to moves list
        #return [i for (i, spot) in enumerate(self.board) if spot == " "]
        #print (moves)
    
    def empty_squares(self):
        return (' ' in self.board)
        
    def num_empty_squares(self):
        return len(self.available_moves())
    
def play(game, x_player, o_player, print_game = True):
    if print_game == True:
        game.print_board_nums()
    
    letter = "X"
        
    while game.empty_squares():
        


  
    
tmp = tic_tac_toe()
tmp.print_board()
tmp.print_board_nums()  
tmp.available_moves()