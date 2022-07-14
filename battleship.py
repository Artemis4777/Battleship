from random import randint

valid_lets = "a b c d e f g h i j"
lets = "abcdefghij"
valid_nums = "1 2 3 4 5 6 7 8 9 10"
num = ""
let = ""
hits = [0]
aircraft_carrier = 5
battleship = 4
destroyer = 3
submarine = 3
patrol_boat = 2
ships = [aircraft_carrier, battleship, destroyer, submarine, patrol_boat]

board = [["0" for i in range(10)] for j in range(10)]
true_board = [["0" for i in range(10)] for j in range(10)]

def randomize(ship):
    nship = str(randint(0, 9))
    nship = nship + str(randint(0, 9))
    nship = nship + str(randint(1, 2))
    nship = nship + ship[3]
    nship = nship + str(randint(1, 2))
    return nship

def set_ships():
    #number, letter, direction, length, backwards
    ship_cords = ["00050", "00040", "00030", "00030", "00020"]
    ship_num = 5
    for shipt in ship_cords:
        while True:
            try:
                cnt = int(shipt[3])
                ship = randomize(shipt)
                if ship[4] == "1":
                    if ship[2] == "1":
                        while cnt > 0:
                            cnt = cnt - 1
                            r_cords =  true_board[int(ship[0]) + cnt][int(ship[1])]
                            if r_cords != "0":
                                cnt = cnt + 1
                                break
                    else:
                        while cnt > 0:
                            cnt = cnt - 1
                            r_cords =  true_board[int(ship[0])][int(ship[1]) + cnt]
                            if r_cords != "0":
                                cnt = cnt + 1
                                break
                else:
                    if ship[2] == "2":
                        while cnt > 0:
                            cnt = cnt - 1
                            r_cords =  true_board[int(ship[0])][int(ship[1]) - cnt]
                            if r_cords != "0" or (int(ship[1]) - cnt) <= 0:
                                cnt = cnt + 1
                                break
                    else:
                        while cnt > 0:
                            cnt = cnt - 1
                            r_cords =  true_board[int(ship[0]) - cnt][int(ship[1])]
                            if r_cords != "0" or (int(ship[0]) - cnt) <= 0:
                                cnt = cnt + 1
                                break
                if cnt == 0:
                    if ship[4] == "1":
                        if ship[2] == "1":
                            cnt = int(ship[3])
                            while cnt > 0:
                                cnt = cnt - 1
                                true_board[int(ship[0]) + cnt][int(ship[1])] = str(ship_num)
                        else:
                            cnt = int(ship[3])
                            while cnt > 0:
                                cnt = cnt - 1
                                true_board[int(ship[0])][int(ship[1]) + cnt] = str(ship_num)
                    else:
                        if ship[2] == "1":
                            cnt = int(ship[3])
                            while cnt > 0:
                                cnt = cnt - 1
                                true_board[int(ship[0]) - cnt][int(ship[1])] = str(ship_num)
                        else:
                            cnt = int(ship[3])
                            while cnt > 0:
                                cnt = cnt - 1
                                true_board[int(ship[0])][int(ship[1]) - cnt] = str(ship_num)
                    ship_num = ship_num + 1
                    break
            except:
                shipt = f"000{ship[3]}0"

def display_board(board):
    print("__________________________________\n|                                |\n|        A B C D E F G H I J     |\n|                                |")
    row_num = 0
    for row in board:
        row_str = ""
        for value in row:
            row_str = row_str + value + " "
        row_num = row_num + 1
        if row_num != 10:
            print("|   ", row_num, " ", row_str, "   |")
        else:
            print("|   ", row_num, "", row_str, "   |\n|                                |")
    print("----------------------------------")

def check_cord(cord):
    cord = cord.lower()
    if cord[0] in valid_lets:
        num = cord[0]
    else:
        return False
    cord = cord.replace(cord[0], "")
    if cord in valid_nums:
        let = cord
    else:
        return False
    return num, let
    
def get_target():
    while True:
        display_board(board)
        shot = input("Where would you like to fire (example = B4)?: ")
        if shot == "Nosson":
            display_board(true_board)
        cords = check_cord(shot)
        if cords == False:
            print("Invalid target. Please check your scopes.")
        else:
            num = cords[1]
            let = cords[0]
            break
    inum = int(num) - 1
    ilet = lets.find(let)
    return inum, ilet

def check_ship(ship):
    if ship < 1:
        print("Sunk!")
    return

def shoot(num, let):
    target = true_board[num][let]
    if target == "0":
        print("Sorry, that missed.")
        board[num][let] = "X"
    elif target == "5":
        print("Hit!")
        board[num][let] = "#"
        true_board[num][let] = "2"
        hits[0] = hits[0] + 1
        ships[0] = ships[0] - 1
        check_ship(ships[0])
    elif target == "6":
        print("Hit!")
        board[num][let] = "#"
        true_board[num][let] = "2"
        hits[0] = hits[0] + 1
        ships[1] = ships[1] - 1
        check_ship(ships[1])
    elif target == "7":
        print("Hit!")
        board[num][let] = "#"
        true_board[num][let] = "2"
        hits[0] = hits[0] + 1
        ships[2] = ships[2] - 1
        check_ship(ships[2])
    elif target == "8":
        print("Hit!")
        board[num][let] = "#"
        true_board[num][let] = "2"
        hits[0] = hits[0] + 1
        ships[3] = ships[3] - 1
        check_ship(ships[3])
    elif target == "9":
        print("Hit!")
        board[num][let] = "#"
        true_board[num][let] = "2"
        hits[0] = hits[0] + 1
        ships[4] = ships[4] - 1
        check_ship(ships[4])
    else:
        print("You already tried that one! Your loss.")

def main():
    print("Here is your board. Let's get started!")
    set_ships()
    count = 0
    while True:
        cords = get_target()
        inum = cords[0]
        ilet = cords[1]
        shoot(inum, ilet)
        count = count + 1
        if hits[0] == 17:
            print(f"You win! It took you {count} shots to sink all the ships.")
            print("Here is your final board.")
            display_board(board)
            break

main()
#set_ships()
#display_board(true_board)
#print(randomize("01251"))
