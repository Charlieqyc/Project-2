# CMPUT 455 sample code
# Alphabeta algorithm
# Template from Eclass code resources


from board_util import (
    GoBoardUtil,
    BLACK,
    WHITE,
    EMPTY,
    BORDER,
    PASS,
    is_black_white,
    is_black_white_empty,
    coord_to_point,
    where1d,
    MAXSIZE,
    GO_POINT
)
from board import GoBoard



INFINITY = 100000
def alphabeta(state,alpha,beta):
    empty_points = state.get_empty_points().size
    gamestate = state.detect_five_in_a_row()
    if empty_points == 0 or (gamestate == BLACK or gamestate == WHITE):
        result = state.getscore(),None
        return result
    legalmoves = state.getBestmove()
    best_move = legalmoves[0]
    for move in legalmoves:
        state.play_move(move,state.current_player)
        cur,_= alphabeta(state, -beta, -alpha)
        cur = -cur
        if cur > alpha:
            alpha = cur
            best_move = move
        state.goBack(move)
        if cur >= beta:
            result = beta, move
            return result
    result = alpha,best_move
    return result

def callalphabeta(rootState):
    return alphabeta(rootState, -INFINITY,INFINITY) 

