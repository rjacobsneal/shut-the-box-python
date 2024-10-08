import sys
from utils import calculate_expected_wins, find_optimal_move


def parse_command_line_args():
    if len(sys.argv) < 4:
        print("Invalid arguments provided.")
        sys.exit(1)

    player = sys.argv[1]  # --one or --two
    operation = sys.argv[2]  # --expect or --move
    position = sys.argv[3]  # string of unique digits like '123456'

    if player not in ["--one", "--two"]:
        print("Player must be --one or --two.")
        sys.exit(1)

    if operation == "--expect":
        if player == "--two":
            if len(sys.argv) != 5:
                print("Player 1's score is required for --two and --expect.")
                sys.exit(1)
            player1_score = int(sys.argv[4])
            return player, operation, position, player1_score
        return player, operation, position

    elif operation == "--move":
        if player == "--one" and len(sys.argv) != 5:
            print("Roll value is required for --one and --move.")
            sys.exit(1)
        elif player == "--two" and len(sys.argv) != 6:
            print("Player 1's score and roll value are required for --two and --move.")
            sys.exit(1)

        roll = int(sys.argv[4]) if player == "--one" else int(sys.argv[5])
        player1_score = int(sys.argv[4]) if player == "--two" else None
        return player, operation, position, player1_score, roll

    else:
        print("Invalid operation. Use --expect or --move.")
        sys.exit(1)


def main():
    args = parse_command_line_args()

    if args[1] == "--expect":
        if args[0] == "--one":
            # player one's expected wins calculation
            expected_wins = calculate_expected_wins(args[2])
        else:
            # player two's expected wins calculation with player 1 score
            expected_wins = calculate_expected_wins(args[2], args[3])
        print(f"{expected_wins:.6f}")

    elif args[1] == "--move":
        if args[0] == "--one":
            # player one's optimal move
            optimal_move = find_optimal_move(args[2], args[4])
        else:
            # player two's optimal move with player 1 score
            optimal_move = find_optimal_move(args[2], args[3], args[4])

        print(f"[{','.join(map(str, sorted(optimal_move)))}]")


if __name__ == "__main__":
    main()
