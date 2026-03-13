def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    n = 5
    play_order = {}

    if len(opponent_history) < n:
        return "R"

    last_five = "".join(opponent_history[-(n):])
    
    potential_plays = [
        "".join(opponent_history[-(n-1):]) + "R",
        "".join(opponent_history[-(n-1):]) + "P",
        "".join(opponent_history[-(n-1):]) + "S",
    ]

    for i in range(len(opponent_history) - n):
        s = "".join(opponent_history[i:i + n])
        if s not in play_order:
            play_order[s] = 0
        play_order[s] += 1

    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    if not sub_order:
        return "P"

    prediction = max(sub_order, key=sub_order.get)[-1]

    ideal_response = {"P": "S", "R": "P", "S": "R"}
    
    return ideal_response[prediction]