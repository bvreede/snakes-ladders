import random

def roll_die():
    return random.randint(1,6)

def check_snakes_ladders(no_in):
    snakes = {
        28: 10,
        39: 18,
        57: 53,
        66: 47,
        92: 33,
        94: 56
        }
    ladders = {
        4: 23,
        7: 12,
        15: 68,
        30: 50,
        36: 41,
        57: 78,
        62: 73,
        86: 89
        }
    if no_in in snakes:
        no_out = snakes[no_in]
    elif no_in in ladders:
        no_out = ladders[no_in]
    else:
        no_out = no_in
    return no_out

# def check_done(no_in):
#     if no_in >= 96:
#         return True
#     else:
#         return False

def play_turn(current):
    #print("Playing a turn starting at", current)
    roll = roll_die()
    #print("Rolling the die to", roll)
    result = current + roll
    result = check_snakes_ladders(result)
    return result

def start_game():
    first = play_turn(1)
    return first

def play_entire_game():
    first = start_game()
    next_result = first
    counter = 1
    while(next_result < 96):
        next_result = play_turn(next_result)
        counter += 1

    #print("Finished after", counter, "turns.")
    return(counter)


if __name__ == "__main__":
    print("Player 1:")
    player_1 = play_entire_game()
    print(player_1, "rolls")

    print("Player 2")
    player_2 = play_entire_game()
    print(player_2, "rolls")

    if player_2 == player_1:
        print("Equal result!")
    elif player_2 < player_1:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

    #for i in range(100):
    #    print(play_entire_game())