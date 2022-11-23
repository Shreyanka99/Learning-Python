# CAR CONTROL GAME USING COMMANDS
command = ""
# stating required initial conditions
start = False
right = False
left = False
stop = False
forward = False
park = False
print('''
Enter instructions to move your car:
        start - begin
        stop - quit game
        help - instructions
        right - moving right
        left - moving left
        forward - going straight
        reverse - taking reverse
        u turn - taking u turn
        quit- leave the program
''')
# checking necessary conditions to continue loop for entering different instructions
while command != 'quit' or command:
    command = input(">>")
    if command == 'help':
        print('''
        start - begin
        stop - quit game
        help - instructions
        right - moving right
        left - moving left
        forward - going straight
        reverse - taking reverse
        u turn - taking u turn''')
# car has started
    elif command == 'start':
        if start:
            print("already started")
        else:
            start = True
            print("started")
# car is asked to stop
    elif command == 'stop' and start:
        print("stopped")
        stop = True
        start = False
# car is asked to move right/left
    elif command == 'right' and start:
        if not right or forward:
            print("taking right")
            right = True
# if car is already taking right, it cant take another right, either a u turn, or moving forward then a right
        elif not forward and right:
            print("already taking right,first move forward and then take right or take U turn ")
    elif command == 'left' and start:
        if not left or forward:
            print("taking left")
            left = True
# car is asked to move forward or reverse
        elif not forward and left:
            print("already taking left,first move forward and then take left")
    elif command == 'forward' and start:
        print("going forward")
        forward = True
# parking the car
    elif command == 'park' and start:
        if not start or park:
            print('already parked')
        else:
            print('parking')
            park = True
# taking U turn
    elif command == 'u turn' and start:
        if (right or left) and not forward:
            print("completing the u turn")
        else:
            print('taking U turn')
# taking reverse
    elif command == 'reverse' and start:
        print('taking reverse')
# leaving the game
    elif command == 'quit':
        exit()
    else:
        print('Start vehicle again // wrong command')
