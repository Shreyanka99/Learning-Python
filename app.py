command = ""
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
''')
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
    elif command == 'start':
        if start:
            print("already started")
        else:
            start = True
            print("started")
    elif command == 'stop' and start:
        print("stopped")
        stop = True
        start = False
    elif command == 'right' and start:
        if not right or forward:
            print("taking right")
            right = True
        elif not forward and right:
            print("already taking right,first move forward and then take right or take U turn ")
    elif command == 'left' and start:
        if not left or forward:
            print("taking left")
            left = True
        elif not forward and left:
            print("already taking left,first move forward and then take left")
    elif command == 'forward' and start:
        print("going forward")
        forward = True
    elif command == 'park' and start:
        if not start or park:
            print('already parked')
        else:
            print('parking')
            park = True
    elif command == 'u turn' and start:
        if (right or left) and not forward:
            print("completing the u turn")
        else:
            print('taking U turn')
    elif command == 'reverse' and start:
        print('taking reverse')
    elif command == 'quit':
        exit()
    else:
        print('Start vehicle again // wrong command')
