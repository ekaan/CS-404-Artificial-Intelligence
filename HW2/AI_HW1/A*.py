from queue import PriorityQueue
import math
import time


class graph:

    def heuristicScore(self,state):  # calculate the heuristic score

        t_x = 4
        t_y = 7  # goal coordinates

        if len(state) == 1:  # if it is in the state one then calculate the heuristic by taking its distance

            x = state[0][0]
            y = state[0][1]

            x_sc = t_x - x
            y_sc = t_y - y

            return math.sqrt( pow(x_sc,2)+pow(y_sc,2) )

        else:  # if it stands on 2 squares

            x1 = state[0][0]
            y1 = state[0][1]

            x2 = state[1][0]
            y2 = state[1][1]

            x_sc1 = t_x - x1
            y_sc1 = t_y - y1

            x_sc2 = t_x - x2
            y_sc2 = t_y - y2

            a = math.sqrt(pow(x_sc1, 2) + pow(y_sc1, 2))  #then take the distance of 2 squares independently then take its average

            b = math.sqrt(pow(x_sc2, 2) + pow(y_sc2, 2))

            return (a+b)/2

    def neighbors(self,state,board):  #returns the successor states as a dictionary

        valid_b = ['S','O','G']  # valid grounds

        result = {}

        if len(state) == 1:  #if it is in the state 1 where it stands in only 1 square

            x = state[0][0]
            y = state[0][1]

            isErr = x-2 < 0 or x-1 < 0 # if there is index error, isError will be true

            if not isErr and board[x-1][y] in valid_b and board[x-2][y] in valid_b: # for up

                result["up"] = [ [x-2, y], [x-1, y] ]    #adds the state corresponding to up to the dictionary

            isErr = y-2 < 0 or y-1 < 0  # if there is index error, isError will be true

            if not isErr and board[x][y-1] in valid_b and board[x][y-2] in valid_b: # for left

                result["left"] = [ [x, y-2], [x, y-1] ]   #adds the state corresponding to left to the dictionary

            isErr = x+2 > 5 or x+1 > 5  # if there is index error, isError will be true

            if not isErr and board[x+1][y] in valid_b and board[x+2][y] in valid_b: # for down

                result["down"] = [ [x+1, y], [x+2, y] ]  #adds the state corresponding to down to the dictionary

            isErr = y+2 > 9 or y+1 > 9  # if there is index error, isError will be true

            if not isErr and board[x][y+1] in valid_b and board[x][y+2] in valid_b: # for right

                result["right"] = [ [x, y+1], [x, y+2] ]  #adds the state corresponding to right to the dictionary




        elif state[0][0] == state[1][0]:

            x1 = state[0][0]
            y1 = state[0][1]

            x2 = state[1][0]
            y2 = state[1][1]

            isErr = x1-1 < 0 or x2-1 < 0   # if there is index error, isError will be true

            if not isErr and board[x1-1][y1] in valid_b and board[x2-1][y2] in valid_b: # for up

                result["up"] = [ [x1-1, y1], [x2-1, y2] ]    #adds the state corresponding to up to the dictionary

            isErr = y1-1 < 0  # if there is index error, isError will be true

            if not isErr and board[x1][y1-1] in valid_b: # for left

                result["left"] = [ [x1, y1-1] ]  #adds the state corresponding to left to the dictionary

            isErr = x1+1 > 5 or x2+1 > 5   # if there is index error, isError will be true

            if not isErr and board[x1+1][y1] in valid_b and board[x2+1][y2] in valid_b: # for down

                result["down"] = [ [x1+1, y1], [x2+1, y2] ]  #adds the state corresponding to down to the dictionary

            isErr = y2+1 > 9   # if there is index error, isError will be true

            if not isErr and board[x2][y2+1] in valid_b: # for right

                result["right"] = [ [x2, y2+1] ]  #adds the state corresponding to right to the dictionary

        elif state[0][1] == state[1][1]:

            x1 = state[0][0]
            y1 = state[0][1]

            x2 = state[1][0]
            y2 = state[1][1]

            isErr = x1-1 < 0   # if there is index error, isError will be true

            if not isErr and board[x1-1][y1] in valid_b: # for up

                result["up"] = [ [x1-1, y1] ]    #adds the state corresponding to up to the dictionary

            isErr = y1-1 < 0 or y2-1 < 0  # if there is index error, isError will be true

            if not isErr and board[x1][y1-1] in valid_b and board[x2][y2-1] in valid_b: # for left

                result["left"] = [ [x1, y1-1], [x2, y2-1] ]   #adds the state corresponding to left to the dictionary

            isErr = x2+1 > 5   # if there is index error, isError will be true

            if not isErr and board[x2+1][y2] in valid_b: # for down

                result["down"] = [ [x2+1, y2] ]  #adds the state corresponding to down to the dictionary

            isErr = y1+1 > 9 or y2+1 > 9   # if there is index error, isError will be true

            if not isErr and board[x1][y1+1] in valid_b and board[x2][y2+1] in valid_b: # for right

                result["right"] = [ [x1, y1+1], [x2, y2+1] ]  #adds the state corresponding to right to the dictionary

        return result

def a_star (graph,s_cd,goal,board):

    visited = []
    queue = PriorityQueue()
    queue.put( (0,s_cd,[],0) )   # puts the starting node to the queue

    while queue:   # while queue is not empty
        cost, state, actions, t_cost = queue.get()  #gets the lowest cost element from queue


        if state not in visited:
            visited.append(state)


            if state in goal:  # if it is the goal state
                return actions,cost   # return how many actions does it need to get to the goal state

            state_neigh = graph.neighbors(state,board)   #gets the state's successors

        #arr = actions[:]

            t_cost = t_cost + 1  # adding one road cost for all of its successors

            for i in state_neigh:  # for its successor states

                if state_neigh[i] not in visited:

                    f_score = t_cost + graph.heuristicScore(state_neigh[i])  # compute the f score

                    a = actions[:]
                    a.append(i)
                    queue.put( (f_score, state_neigh[i], a, t_cost) )  # put the successor to queue



#=================== Main Function ==============================

start = time.time()   # starts the timer

board = [['O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],  # specify the game board
         ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X'],
         ['O', 'O', 'O', 'S', 'O', 'O', 'O', 'O', 'O', 'X'],
         ['X', 'O', 'O', 'S', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'G', 'O', 'O'],
         ['X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X']]

s_cd1 = [[1, 1]] #specify the starting state

goal1 = [[[4, 5], [4, 6]], [[2, 7], [3, 7]], [[4, 8], [4, 9]]] # specify the goal states

gr1 = graph()   # create the graph

sequence,t_cost = a_star(gr1,s_cd1,goal1,board)

Final_seq = ""

for i in sequence:
    Final_seq += i + "-"

print("Total cost is: " + str( len(sequence) ))
print("Final sequence is: " + Final_seq[:len(Final_seq)-1])  # print the results
print("Total time:", time.time() - start)


