board = [
    [0,5,4, 8,0,0, 0,9,0],
    [0,0,0, 5,0,0, 7,0,3],
    [8,9,0, 2,1,0, 4,0,0],

    [0,3,0, 7,0,0, 5,0,9],
    [2,0,0, 4,0,6, 0,0,7],
    [9,0,6, 0,0,5, 0,1,0],

    [0,0,7, 0,3,8, 0,4,1],
    [6,0,1, 0,0,2, 0,0,0],
    [0,8,0, 0,0,4, 6,2,0]
]

# index_classifier = [
#     [(0,1,2),(0,1,2)], [(0,1,2),(3,4,5)], [(0,1,2),(6,7,8)],
#     [(3,4,5),(0,1,2)], [(3,4,5),(3,4,5)], [(3,4,5),(6,7,8)],
#     [(6,7,8),(0,1,2)], [(6,7,8),(3,4,5)], [(6,7,8),(6,7,8)]
# ]

def print_board():
    for row in board:
        print(row)

print_board()


def get_square(position):
    r = position[0]
    c = position[1]

    row_of_square = r // 3
    col_of_square = c // 3

    return (row_of_square, col_of_square)


def can_exist_in_row(position, proposed_num):
    '''
    Returns (Can exist?, Position if cannot exist (row,col))
    '''

    if board[position[0]][position[1]] != 0:
            raise ValueError("Proposed number slot is already taken.")

    for row in range(0,9):
        if proposed_num == board[row][position[1]]:
            return False
            return (False, (row, position[1]))
        
        return True
        return (True, None)

def can_exist_in_col(position, proposed_num):
    if proposed_num in board[position[1]]:
        for col in range(0,9):
            if proposed_num == board[position[1]][col]:
                return False
                return (False, (position[1],col))
    
    return True
    return (True, None)

def can_exist_in_square(position, proposed_num):
    row = get_square(position)[0]
    col = get_square(position)[1]

    for row_index in range(row, row+3):
        for col_index in range(col, col+3):
            if proposed_num == board[row_index][col_index]:
                return False
                return (False, (row_index, col_index))

    return True
    return (True, None)


def can_proposition_exist(position, proposed_num):
    print(can_exist_in_row(position, proposed_num))
    print(can_exist_in_col(position, proposed_num))
    print(can_exist_in_square(position, proposed_num))

    return can_exist_in_row(position, proposed_num) and can_exist_in_col(position, proposed_num) and can_exist_in_square(position, proposed_num)


print(can_proposition_exist((0,4), 1))