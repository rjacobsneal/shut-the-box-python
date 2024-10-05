from itertools import combinations


def calculate_expected_wins(position, player1_score=None):
    """
    Calculate the expected number of wins based on the current position.
    For --two, consider player1_score.
    """
    # Placeholder for actual implementation
    # You would need to calculate expected wins based on game rules
    if player1_score:
        # Calculation when it's player two's turn
        pass
    else:
        # Calculation when it's player one's turn
        pass

    return 0.5  # Example return value (replace with actual logic)


def find_optimal_move(position, roll, player1_score=None):
    """
    Find the optimal move (list of tiles to close) given the current position and roll.
    For --two, consider player1_score.
    """
    remaining_tiles = list(map(int, list(position)))

    # Get all possible combinations of remaining tiles that sum to the roll
    possible_moves = [
        combo
        for i in range(1, len(remaining_tiles) + 1)
        for combo in combinations(remaining_tiles, i)
        if sum(combo) == roll
    ]

    if not possible_moves:
        return []  # No valid moves, should not happen per problem constraints

    # Placeholder for determining the best move
    optimal_move = possible_moves[
        0
    ]  # Replace with actual logic to determine optimal move

    return list(optimal_move)
