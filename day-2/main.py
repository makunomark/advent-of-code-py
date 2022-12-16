from enum import Enum

print("--- Day 2: Rock Paper Scissors ---")

read_file = open("input.txt", "r")
lines = read_file.readlines()

class Symbol(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# opponent
# A: Rock
# B: Paper
# C: Scissors
class Opponent(Enum):
    A= Symbol.ROCK
    B= Symbol.PAPER
    C= Symbol.SCISSORS

# player
# X: Rock
# Y: Paper
# Z: Scissors
class Player(Enum):
    X= Symbol.ROCK
    Y= Symbol.PAPER
    Z= Symbol.SCISSORS

# shape score
# Rock: 1
# Paper: 2
# Scissors: 3
class SymbolScore(Enum):
    ROCK= 1
    PAPER= 2
    SCISSORS= 3

# result score
# lose: 0
# draw: 3
# win: 6
class ResultScore(Enum):
    LOSE= 0
    DRAW= 3
    WIN= 6

def play(input):
    opponent = input.split(" ")[0]
    player = input.split(" ")[1]
    score_this_round = 0
    score_this_round += SymbolScore[Player[player].value.name].value
    if Opponent[opponent].value == Player[player].value:
        score_this_round += ResultScore.DRAW.value
    elif Player[player].value == Symbol.ROCK and Opponent[opponent].value == Symbol.SCISSORS:
        score_this_round += ResultScore.WIN.value
    elif Player[player].value == Symbol.PAPER and Opponent[opponent].value == Symbol.ROCK:
        score_this_round += ResultScore.WIN.value
    elif Player[player].value == Symbol.SCISSORS and Opponent[opponent].value == Symbol.PAPER:
        score_this_round += ResultScore.WIN.value
    else:
        score_this_round += ResultScore.LOSE.value
    
    return score_this_round

# strategy
# X: Lose
# Y: Draw
# Z: Win
class Strategy(Enum):
    X= ResultScore.LOSE
    Y= ResultScore.DRAW
    Z= ResultScore.WIN

# Symbol beats
class SymbolBeats(Enum):
    ROCK= Symbol.SCISSORS
    PAPER= Symbol.ROCK
    SCISSORS= Symbol.PAPER

# Symbol loses
class SymbolLoses(Enum):
    ROCK= Symbol.PAPER
    PAPER= Symbol.SCISSORS
    SCISSORS= Symbol.ROCK

# player_inverse = Player.inverse

def get_player_move(strategy, opponents_move):
    print(strategy, opponents_move)
    if strategy == ResultScore.LOSE:
        return SymbolBeats[opponents_move.name].value
    elif strategy == ResultScore.DRAW:
        return opponents_move
    else:
        return SymbolLoses[opponents_move.name].value

def play_part_2(input):
    score_this_round = 0
    opponent = input.split(" ")[0]
    strategy = input.split(" ")[1]
    mapped_strategy = Strategy[strategy].value

    player_move = get_player_move(mapped_strategy, Opponent[opponent].value)
    score_this_round += SymbolScore[player_move.name].value
    score_this_round += ResultScore[mapped_strategy.name].value
    print("player:", strategy, mapped_strategy, "player:", player_move, "opponent:", Opponent[opponent].value)
    print("score_this_round:", score_this_round)
    return score_this_round



def main(part):
    total_score = 0
    total_score_part_2 = 0
    for line in lines:
        if part == 0:
            score_this_round = play(line.strip())
            total_score += score_this_round
            print("Score this round:", score_this_round)
        else:
            print("_______________________")
            total_score_part_2 += play_part_2(line.strip())

    if part == 0:
         print("Total score:", total_score)
    else:
        print("\n")
        print("Total score:",total_score_part_2)

for part in range(2):
    if part == 0:
        print("--- Part One ---")
    else:
        print("\n")
        print("--- Part Two ---")
    main(part)
