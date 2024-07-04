

chess_board = []
f = open("input.txt", "r")
for line in f:
    row = []
    for it in line.strip().split(' '):
        row.append(it)
    chess_board.append(row)

posi = []

def findQueen(chess_board,i):
    count = 1
    queenPos = []
    for line in chess_board:
        #print(line[0])
        for pos in line[i]:
            if pos == 'Q':
                posi.append(count)
            count += 1
#lấy vị trí của tất cả các queen
findQueen(chess_board,0)
findQueen(chess_board,1)
findQueen(chess_board,2)
findQueen(chess_board,3)
findQueen(chess_board,4)
findQueen(chess_board,5)
findQueen(chess_board,6)
findQueen(chess_board,7)
print(posi)

fight = 0

def heuristic():
    
        