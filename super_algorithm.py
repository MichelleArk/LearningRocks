import random

def random_rps():
    return random.randint(0,2)

def update_history(choice, prev_choice, outcome):
    # rock = 0; paper = 1; scissors = 2;
    if (choice, prev_choice, outcome) in me_history:
        me_history[(choice, prev_choice, outcome)] += 1
    else:
        me_history[(choice, prev_choice, outcome)] = 1

    if (prev_choice, outcome) in total_history:
        total_history[(prev_choice, outcome)] += 1
    else:
        total_history[(prev_choice, outcome)] = 1

def make_decision(player_prev_choice, player_outcome):
    # prob of player playing i
    probs = []
    for i in range(3):
        if (i,player_prev_choice,player_outcome) not in me_history:
            me_history[(i,player_prev_choice,player_outcome)] = 0
            probs.append(0)
        else:
            probs.append(float(me_history[(i, player_prev_choice, player_outcome)]) / total_history[(player_prev_choice, player_outcome)])
    if sum(probs) == 0:
        return random_rps()
    return (max_index(probs) + 1) % 3

def max_index(prob_list):
    max_prob = 0
    index = -1
    for i in range(len(prob_list)):
        if prob_list[i] > max_prob:
            max_prob = prob_list[i]
            index = i
    return index

#return if p1 loses, ties, or wins
def get_outcome(p1, p2):
    # -1: loss; 0: tie; 1: win
    if p1 == p2:
        print("Tie!")
        return 0
    elif p1 == (p2 + 1) % 3:
        print("You Win!")
        return 1
    else:
        print("muahaha")
        return -1

def get_player_move():
    move = raw_input('Play r/p/s: ')
    while move not in rps_to_int:
        move = raw_input('Play r/p/s: ')
    return rps_to_int[move]

if __name__ == "__main__":

    rps_to_int = {"r":0,"p":1,"s":2}
    int_to_rps = {0:"r", 1:"p", 2:"s"}
    total_history = {}
    me_history = {}

    # first iteration
    first_me = get_player_move()
    computer = random_rps()
    print("Computer plays: " + int_to_rps[computer])
    first_outcome = get_outcome(first_me, computer)

    # second iteration
    me = get_player_move()
    computer = random_rps()
    print("Computer plays: " + int_to_rps[computer])
    # second choice given first choice and first outcome
    update_history(me, first_me, first_outcome)
    outcome = get_outcome(me, computer)

    total_games = 0
    computer_wins = 0
    while True:
        prev_choice = me
        me = get_player_move()
        computer = make_decision(prev_choice, outcome)
        print("Computer plays: " + int_to_rps[computer])
        update_history(me, prev_choice, outcome)
        outcome = get_outcome(me, computer)
        if outcome == -1:
            computer_wins += 1
        total_games += 1
        print(float(computer_wins) / total_games)
