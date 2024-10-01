import random
import matplotlib.pyplot as plt

def main():
    #print average difference of delta for 2 players
    average_difference = simulate_monopoly_games(10000)
    print(f"Monopoly simulator: two players, 1500 euro starting money, 10000 games \nOn average player 1 has {average_difference} more streets in their possession when all streets have been bought")

    # obtain the result by looking at the graph and print
    print(f"Monopoly simulator: 2 players \nOn average, if player 2 receives 150 euros more starting money, both players collect an equal number of streets")
    equilibrium()

def throw_two_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    return sum

# simulate monopoly function
def simulate_monopoly(starting_money_p1 = 1500, starting_money_p2 = 1500):

    # define pre-loop variables
    positions = [0, 0]
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                0, 320, 200, 0, 350, 0, 400]
    posessions = [0] * 40
    throw_count = 0
    money = [starting_money_p1, starting_money_p2]


    # use a for loop to loop around each throw
    for x in range(0, 1000):
        while (posessions.count(1) + posessions.count(2)) < 28:
            positions[0] = positions[0] + throw_two_dice()
            positions[1] = positions[1] + throw_two_dice()

            # fix positon > 39 and add money for passing start for each player
            if positions[0] > 39:
                positions[0] = (positions[0] % 39) - 1
                money[0] += 200

            if positions[1] > 39:
                positions[1] = (positions[1] % 39) - 1
                money[1] += 200


            # acquire a property if not already aquired and have enough money for p1
            if board_values[positions[0]] != 0 and posessions[positions[0]] == 0 and money[0] > board_values[positions[0]]:
                posessions[positions[0]] = 1
                # substract money
                money[0] -= board_values[positions[0]]

            # acquire a property if not already aquired and have enough money for p2
            if board_values[positions[1]] != 0 and posessions[positions[1]] == 0 and money[1] > board_values[positions[1]]:
                posessions[positions[1]] = 2
                # substract money
                money[1] -= board_values[positions[1]]


            #print(f"P1 position: {positions[0]}, money: {money[0]}, properties: {posessions.count(1)} \n P2 position: {posessions.count(2)}, money: {money[1]}, properties: {posessions.count(2)} ")


    delta = posessions.count(1) - posessions.count(2)
    return (delta)


# simulate monopoly games function
def simulate_monopoly_games(total_games, start_money_p1 = 1500, start_money_p2 = 1500 ):
    a_list = []
    for game in range(0, total_games):
        delta = simulate_monopoly(start_money_p1, start_money_p2)
        a_list.append(delta)
    average_difference = sum(a_list) / total_games
    return average_difference

def equilibrium():
    value_list = [1500, 1550, 1600, 1650, 1700]
    delta_list = []
    for x in value_list:
        delta = simulate_monopoly_games(10000, 1500, x)
        delta_list.append(delta)
    plt.plot(value_list, delta_list)
    plt.axhline(0)
    plt.show()

if __name__ == "__main__":
    main()
