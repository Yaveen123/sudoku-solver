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

def print_board_custom(board):
    for row in board:
        print(row)
    


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
    return can_exist_in_row(position, proposed_num) and can_exist_in_col(position, proposed_num) and can_exist_in_square(position, proposed_num)

def get_candidates():
    all_candidates = []
    for row in range(0,9):
        all_candidates_for_col = []

        for col in range(0,9):

            all_candidates_for_cell = []
            for candidate in range(1,10):
                try:
                    if can_proposition_exist((row,col), candidate):
                        all_candidates_for_cell.append(candidate)
                except:
                    pass

            all_candidates_for_col.append(all_candidates_for_cell)    

        all_candidates.append(all_candidates_for_col)

    return all_candidates


def is_board_solved(candidates):
    if get_min_length_of_candidates(candidates) == 100:
        return True
    return False

def get_min_length_of_candidates(candidates):
    min_length = 100
    for row in candidates:
        for col in row:
            if len(col) < min_length and len(col) > 0:
                min_length = len(col)

    return min_length



def is_board_valid(): 
    pass


min_length_seen = 0

def get_cell_to_solve(candidates, min_length):
    for row in range(0,9):
        for col in range(0,9):
            if len(candidates[row][col]) == min_length and len(candidates[row][col]) > 0:
                return (row, col)

    return False

def solver():
    # Check if board is solved by finding all available candidates
    candidates = get_candidates()
    if is_board_solved(candidates):
        print("a. Board solved!")
        print_board_custom(board)
        return board    
    
    # Get the row/col of the cell with the smallest number of candidates. 
    # If there are no more cells, then the board is solved
    row, col = (None, None)
    try:
        row, col = get_cell_to_solve(candidates, get_min_length_of_candidates(candidates))
    except TypeError:
        print_board_custom(board)
        print("b. Board solved!")
    finally:
        if row == None or col == None:
            raise RuntimeError("Solver has reached an unexpected state where the cell selected is invalid or no cell could be selected.")

    candidates_for_cell = candidates[row][col]

    for proposed_num in candidates_for_cell:
        board[row][col] = proposed_num

        if solver():
            return True

        board[row][col] = 0
    
    return False

for i in get_candidates():
    print(i)

solver()
# ADD THIS LINE:
print("\n--- Final Board State ---")
print_board() # Or print_board_custom(board)


