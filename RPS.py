def player(prev_play, opponent_history=[], play_history={}):
    if not prev_play:
        prev_play = 'R'

    # Append the opponent's previous play to their history
    opponent_history.append(prev_play)
    
    # Default prediction
    prediction = 'P'

    # Update play_history with the last five moves
    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        play_history[last_five] = play_history.get(last_five, 0) + 1
        
        # Generate potential plays based on the last four moves and each possible next move
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        # Find the most frequent move in the potential plays
        sub_order = {
            k: play_history[k]
            for k in potential_plays if k in play_history
        }

        # Track the most frequent move
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    # Pick the ideal response based on the most frequent move
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]