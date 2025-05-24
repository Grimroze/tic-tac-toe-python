def win(curr_game, n):
    winners = []

    def test(line, label):
        if len(line) == line.count(line[0]) and line[0] != " ":
            winners.append(f"Winner {label}: Player {line[0]}")

    # Check rows
    for row in curr_game:
        test(row, "horizontally")

    # Check columns
    for col in range(n):
        col_vals = [curr_game[row][col] for row in range(n)]
        test(col_vals, "vertically")

    # Check main diagonal
    main_diag = [curr_game[i][i] for i in range(n)]
    test(main_diag, "diagonal (\\)")

    # Check anti-diagonal
    anti_diag = [curr_game[i][n - 1 - i] for i in range(n)]
    test(anti_diag, "diagonal (/)")

    if winners:
        for result in winners:
            print(result)
        return True
    return False

def game_board(game_map, n, player_symbol=" ", row=0, column=0, just_display=False):
    try:
        print("   " + "  ".join(map(str, range(n))))
        if not just_display:
            if game_map[row][column] != " ":
                print("Occupied bruh, choose another")
                return game_map, False
            game_map[row][column] = player_symbol
        for count, row in enumerate(game_map):
            print(f"{count} {row}")
        return game_map, True

    except IndexError:
        print("Error: use only valid row/column numbers!")
        return game_map, False

    except Exception as e:
        print("Unexpected error occurred!", e)
        return game_map, False

# Main game loop
play = True
while play:
    try:
        n = int(input("Enter board size (e.g. 3 for 3x3): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    game = [[" " for _ in range(n)] for _ in range(n)]
    game_won = False
    game, _ = game_board(game, n, just_display=True)
    player_symbols = ["X", "O"]
    curr_player = 0
    move_count = 0
    total_moves = n * n

    while not game_won and move_count < total_moves:
        print(f"\nPlayer {curr_player + 1} ({player_symbols[curr_player]})'s turn")
        played = False
        while not played:
            try:
                row_choice = int(input(f"Enter row (0 to {n-1}): "))
                col_choice = int(input(f"Enter column (0 to {n-1}): "))
            except ValueError:
                print("Please enter valid numbers!")
                continue

            game, played = game_board(game, n, player_symbols[curr_player], row_choice, col_choice)

        move_count += 1
        game_won = win(game, n)

        if not game_won:
            curr_player = 1 - curr_player

    if not game_won and move_count == total_moves:
        print("It's a draw!")

    again = input("\nWanna play again? (y/n): ").lower()
    if again != "y":
        play = False
        print("Thanks for playing!")
