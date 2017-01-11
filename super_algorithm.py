import random

def random_rps():

    random_num = random.randint(0,2)

    return random_num

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
        probs.append(me_history[(i, player_prev_choice, player_outcome)] / total_history[(player_prev_choice, player_outcome)])

    assert sum(probs) == 1

    return max_index(probs)

def max_index(prob_list):
    max_prob = 0
    index = -1
    for i in range(len(prob_list)):
        if prob_list[i] > max_prob:
            max_prob = prob_list[i]
            index = i

    return (i, max_prob)
if __name__ == "__main__":

    total_history = {}
    me_history = {}
    computer_history = {}

    while True:
        me = raw_input('Play your game: ')
        computer = random_rps()

        me_history.append(me)
        computer_history.append(computer)

        print('Me: {} || Computer: {}'.format(me, computer))
