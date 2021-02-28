from board_util import BLACK, WHITE, EMPTY

score_set = [0, 1, 2, 5, 15, 10000]


def countColorInFive(board, line):
    blackCount = 0
    whiteCount = 0
    for point in line:
        # get the color of specific point according to a single number represented in board_util file
        # for example
        #     16   17 18 19   20
        #
        #     12   13 14 15
        #     08   09 10 11
        #     04   05 06 07
        #
        #     00   01 02 03
        curColor = board.board[point]
        if curColor == BLACK:
            blackCount += 1
        elif curColor == WHITE:
            whiteCount += 1
    return blackCount, whiteCount



def score(countOutCome, color):
    # since we only detect five points per time, if there is at least one white point and one black point,
    # there will not be a chance to find five stones with the same color in a line
    if countOutCome[0] >= 1 and countOutCome[1] >= 1:
        return 0
    if color == BLACK:
        bc = countOutCome[0]
        wc = countOutCome[1]
    else:
        bc = countOutCome[1]
        wc = countOutCome[0]
    return score_set[bc] - score_set[wc]


def evaluate(board, color):
    value = 0
    lines = board.rows + board.cols + board.diags
    # traverse every possible line on the board
    for line in lines:
        # edge detection, and traverse all the possible combination of black and white on a line
        # for example: in row1 aa?bb?a, it will have 3 combination: aa?bb,a?bb?,?bb?a, it will give us different count
        for i in range(0, len(line) - 5):
            countOut = countColorInFive(board, line[i:i + 5])
            value += score(countOut,color)
    return value
