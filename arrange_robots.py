#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Spring 2021
#


import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Count total # of pichus on board
def count_pichus(board):
    return sum([ row.count('p') for row in board ] )

# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col):
    return board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:]

            
# Get list of successors of given board state
def successors(board):
   for r in range(0, len(board)):
        for c in range(0,len(board[0])):
            if board[r][c] == '.':
                i=c
                left_position=False
                #While loop checks if it encounters any X's or @'s before a 'p' to the left of the current (row,col) position.
                while(i>=0):  
                    if board[r][i]=="X" or board[r][i]=="@" :
                        left_position=True
                        break
                    if board[r][i]=="p":
                        left_position=False
                        break
                    i-=1
                if (i<0):
                    left_position=True 
                if left_position==False:
                   continue
                i=c
                right_position=False
                #While loop checks if it encounters any X's or @'s before a 'p' to the right of the current (row,col) position.
                while(i<len(board[0])):
                    if board[r][i]=="X" or board[r][i]=="@":
                        right_position=True
                        break
                    if board[r][i]=="p":
                        right_position=False
                        break
                    i+=1
                if (i>=len(board[0])):
                    right_position=True
                if right_position==False:
                   continue
                i=r
                Up_position=False
                #While loop checks if it encounters any X's or @'s before a 'p' to the top of the current (row,col) position.
                while(i>=0):
                    if board[i][c]=="X" or board[i][c]=="@":
                        Up_position=True
                        break
                    if board[i][c]=="p":
                        Up_position=False
                        break
                    i-=1
                if (i<0):
                    Up_position=True
                if Up_position==False:
                   continue
                i=r
                down_position=False
                #While loop checks if it encounters any X's or @'s before a 'p' to the bottom of the current (row,col) position.
                while(i<len(board)):
                    if board[i][c]=="X" or board[i][c]=="@":
                        down_position=True
                        break
                    if board[i][c]=="p":
                        down_position=False
                        break
                    i+=1 
                if (i>=len(board)):
                    down_position=True              
                if down_position==False:
                   continue
               #If there are no conflicts with the current location(row,col) and other p's in the board then we call the add_pichu function to add a 'P' in this (r,c) location on the board.
                if (left_position and right_position and Up_position and down_position):
                    return [add_pichu(board, r, c)]
    
   return []
                
# check if board is a goal state
def is_goal(board, k):
    return count_pichus(board) == k 
 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):
    fringe = [initial_board]
    
    while len(fringe) > 0:
        for s in successors(fringe.pop(0)): #Remove the first element from the fringe 
            if is_goal(s, k):
                return(s,True)
            fringe.append(s)
    return ([],False)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print ("Here's what we found:")
    print (printable_board(newboard) if success else "None")


