

def render(board_width, board_height, shots):
    header = "+" + "-" * board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if(x, y) in shots_set:
                shots_marker = 'X'
            else:
                shots_marker = ' '
            row.append(shots_marker)
        print('|' + "".join(row) + "|")

    print(header)

if __name__ == '__main__':
    shots = []

    while True:
        player_coordinates = input('Please enter your firing coordinates: ')
        # TODO: incorporate a means of validating player input.
        xstr, ystr = player_coordinates.split(',')
        x = int(xstr)
        y = int(ystr)

        shots.append((x, y))
        render(10, 10, shots)

