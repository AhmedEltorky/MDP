# the maze
# \ 0 \ 0 \ 0 \  100 \
# \ 0 \ # \ 0 \ -100 \
# \ 0 \ 0 \ 0 \   0  \

# East ==> c + 1
# West ==> c - 1
# North ==> r - 1
# South ==> r + 1

# q_east = (0.8*v[r][c+1]) + (0.1*v[r-1][c]) + (0.1*v[r+1][c]) - 3
# q_west = (0.8*v[r][c-1]) + (0.1*v[r-1][c]) + (0.1*v[r+1][c]) - 3
# q_north = (0.8*v[r-1][c]) + (0.1*v[r][c+1]) + (0.1*v[r][c-1]) - 3
# q_south = (0.8*v[r+1][c]) + (0.1*v[r][c+1]) + (0.1*v[r][c-1]) - 3

EAST = 0
WEST = 1
NORTH = 2
SOUTH = 3

REWARD = 0  # (-1, -3, -40, -200)
GAMA = 0.9


def set_policy(value, pr, pc, direction):
    policy[pr][pc][0] = value
    if direction is EAST:
        policy[pr][pc][1] = "East"
    elif direction is WEST:
        policy[pr][pc][1] = "West"
    elif direction is NORTH:
        policy[pr][pc][1] = "North"
    elif direction is SOUTH:
        policy[pr][pc][1] = "South"


def get_row(row):
    if row < 0:
        return 0
    elif row > 2:
        return 2
    else:
        return row


def get_column(column):
    if column > 3:
        return 3
    elif column < 0:
        return 0
    else:
        return column


def get_v(row, column, direction):
    if row == column == 1:
        if direction == WEST:
            return v[row][column + 1]
        elif direction == EAST:
            return v[row][column - 1]
        elif direction == NORTH:
            return v[row + 1][column]
        elif direction == SOUTH:
            return v[row - 1][column]
    else:
        return v[row][column]


def get_max_q_value(qr, qc):
    # return max(q[qr][qc])
    max_q = -100000
    direction = -1
    for i in q[qr][qc]:
        direction += 1
        if i > max_q:
            max_q = i
            max_dir = direction
    set_policy(max_q, qr, qc, max_dir)
    return max_q


# REWARD = input("please enter reward value:")
# iterations = input("please enter number of iterations:")

# initial value of value iteration
v = [[0, 0, 0, 100], [0, "Block", 0, -100], [0, 0, 0, 0]]

reward_function = ((REWARD, REWARD, REWARD, 100), (REWARD, "Block", REWARD, -100), (REWARD, REWARD, REWARD, REWARD))

q = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 100],
     [[0, 0, 0, 0], "Block", [0, 0, 0, 0], -100],
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

policy = [[[0, 0], [0, 0], [0, 0], ["GEM"]],
          [[0, 0], ["BLOCK"], [0, 0], ["FIRE"]],
          [[0, 0], [0, 0], [0, 0], [0, 0]]]

# tests:
# print(get_max_q_value(2, 2))
# print(q[1][0][WEST])
# print(v[1][1])
# print(get_v(1, 1, EAST))

for iteration in range(100):
    for r in range(3):
        for c in range(3, -1, -1):
            # print(r, c)
            if not (r == 0 and c == 3):
                if not (r == 1 and c == 3):
                    if not (r == 1 and c == 1):
                        q[r][c][EAST] = GAMA * ((0.8 * get_v(r, get_column(c + 1), EAST)) + \
                                                (0.1 * get_v(get_row(r - 1), c, EAST)) + (0.1 * get_v(get_row(r + 1), c, EAST))) + REWARD

                        q[r][c][WEST] = GAMA * ((0.8 * get_v(r, get_column(c - 1), WEST)) + \
                                                (0.1 * get_v(get_row(r - 1), c, WEST)) + (0.1 * get_v(get_row(r + 1), c, WEST))) + REWARD

                        q[r][c][NORTH] = GAMA * ((0.8 * get_v(get_row(r - 1), c, NORTH)) + (0.1 * get_v(r, get_column(c + 1), NORTH)) + \
                                                (0.1 * get_v(r, get_column(c - 1), NORTH))) + REWARD

                        q[r][c][SOUTH] = GAMA * ((0.8 * get_v(get_row(r + 1), c, SOUTH)) + (0.1 * get_v(r, get_column(c + 1), SOUTH)) + \
                                                (0.1 * get_v(r, get_column(c - 1), SOUTH))) + REWARD

                        v[r][c] = get_max_q_value(r, c)

    print("The value of iteration", iteration + 1, ":")
    for x in v:
        print(x)
    print()

    print("The Q value of iteration", iteration + 1, ":")
    for y in q:
        print(y)
    print()

    print("The Policy of iteration", iteration + 1, ":")
    print(policy[0][0], policy[0][1], policy[0][2], policy[0][3])
    print(policy[1][0], policy[1][1], policy[1][2], policy[1][3])
    print(policy[2][0], policy[2][1], policy[2][2], policy[2][3])
    print()
