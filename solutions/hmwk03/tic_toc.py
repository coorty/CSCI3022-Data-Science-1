# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:39:42 2017

@author: Administrator
"""

import numpy as np

def is_win(_dices, win_tie_lines):
    state = list(map(lambda x: sum([1 for i in _dices if i in x]), win_tie_lines))
    return False + state.count(3)
    
def put_dice(board, _dices):
    idx = np.random.randint(len(board))
    dice = board[idx]  # 落子的地方
    _dices.append(dice)
    board.pop(idx)

win_tie_lines = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

exper_num = 100000
win_list = [0]*exper_num
for i in range(exper_num):
    X_dices, O_dices = [], []
    board = list(range(1,10))
    num_X, num_O = 0, 0
    board_state = False
    
    while board_state == False:
        # X 先下
        num_X += 1
        put_dice(board, X_dices)
        
        if num_X >= 3:
            board_state = is_win(X_dices, win_tie_lines)
            if board_state > 0:
                win_list[i] = 1
                break
            
        if num_X + num_O == 9:
            break
            
        # O 后下
        num_O += 1
        put_dice(board, O_dices)    
        if num_O >= 3:
            board_state = is_win(O_dices, win_tie_lines)
            if board_state > 0:
                win_list[i] = -1
                break
    
print('X win '+str(win_list.count(1))+' ; '+str(win_list.count(1)/exper_num))
print('O win '+str(win_list.count(-1))+' ; '+str(win_list.count(-1)/exper_num))    
print('Draw  '+str(win_list.count(0))+' ; '+str(win_list.count(0)/exper_num)) 
    


















