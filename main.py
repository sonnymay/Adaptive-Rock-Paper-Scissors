import random

def get_user_input():
    while True:
        user_input = input("Choose rock (r), paper (p), or scissors (s): ")
        if user_input.lower() in ['r', 'p', 's']:
            return user_input.lower()
        else:
            print("Invalid input. Please try again.")

def get_ai_move(move_frequencies):
    moves = ['r', 'p', 's']
    if sum(move_frequencies.values()) == 0:
        return random.choice(moves)
    else:
        move_probabilities = {move: freq / sum(move_frequencies.values()) for move, freq in move_frequencies.items()}
        counter_moves = {'r': 'p', 'p': 's', 's': 'r'}
        return counter_moves[max(move_probabilities, key=move_probabilities.get)]

def update_frequencies(move_frequencies, user_move):
    move_frequencies[user_move] += 1

def game_result(user_move, ai_move):
    if user_move == ai_move:
        return "draw"
    elif (user_move == 'r' and ai_move == 's') or (user_move == 'p' and ai_move == 'r') or (user_move == 's' and ai_move == 'p'):
        return "user"
    else:
        return "ai"

def main():
    move_frequencies = {'r': 0, 'p': 0, 's': 0}
    score = {'user': 0, 'ai': 0, 'draw': 0}
    
    print("Welcome to the Rock-Paper-Scissors game!")
    
    while True:
        user_move = get_user_input()
        ai_move = get_ai_move(move_frequencies)
        
        print(f"User move: {user_move}")
        print(f"AI move: {ai_move}")
        
        result = game_result(user_move, ai_move)
        update_frequencies(move_frequencies, user_move)
        score[result] += 1
        
        print(f"Result: {result.capitalize()} wins!")
        print(f"Score: User {score['user']} - AI {score['ai']} (Draws: {score['draw']})")
        
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
