#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys
import json

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

	# Return only moves that are within the board and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

#Finds the direction in which agent has moved and returns a string in the form of L,R,D,U for the directions left,right,down,up respectively 
def direction(next_move,curr):
    if next_move[0]>curr[0]:  # checks if the row of the current position of the agent is greater than the previous position, if yes then it has moved down
        return "D"
    elif next_move[1]>curr[1]:  # checks if the column of the current position of the agent is greater than the previous position, if yes then it has moved right
        return "R"
    elif next_move[0]<curr[0]:  # checks if the row of the current position of the agent is lesser than the previous position, if yes then it has moved up
        return "U"
    elif next_move[1]<curr[1]:  # checks if the column of the current position of the agent is lesser than the previous position, if yes then it has moved left
        return "L"

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#
    
def search(house_map):
        visited_nodes=[] #Contains a list of all nodes that have already been visited ----
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0,"")] # pichu_loc contains the location of the agent and 0 is passed for the initial path length and an empty string is passed as there is the agent is yet to move in a particular direction
        new_move_string="" # Holds the string which is the set of directions for the agent to reach that particular location on the board
        while fringe:
                (curr_move, curr_dist,move_string)=fringe.pop(0) # Removes the first element in the queue
                for move in moves(house_map, *curr_move):
                        if house_map[move[0]][move[1]]=="@": #checks if the agent has reached the goal state
                                curr_dist+=1                 # curr_dist holds the path length and it is incremented by one for each move 
                                move_string+=direction(move,curr_move) #calls the direction function which returns a string which contains the direction in which the agent has moved
                                return (curr_dist,move_string)
                        else:
                                if move not in visited_nodes:    # checks if the node was already visited 
                                    new_move_string=move_string+direction(move,curr_move) # adds the direction in which the agent moves to the string of directions it has already moved until this point
                                    fringe.append((move, curr_dist + 1,new_move_string))  # the fringe is appended with the new move of the agent with the path lenght and the directions as well
                                    new_move_string=""                                    # the string is empty before every loop because the agent moves different directions after each loop
                                    visited_nodes.append(move) 
        return (-1,"")

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Routing in this board:\n" + printable_board(house_map) + "\n")
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + str(solution[1]))

