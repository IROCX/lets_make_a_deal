import random

def game(switcher):

    doors = [1,2,3]

    #player chooses a random door

    car_door = random.randint(1,3)
    player_initial_choice = random.randint(1,3)

    #monty opens a door having goat by elimination

    host_door = [1,2,3]
    
    #removed player's first choice

    host_door.remove(player_initial_choice)

    #remove the car_door
    if (car_door in host_door[0]):
        host_door.remove(car_door)
    else:
        host_door.remove(random.choice(host_door))

    #player decides to switch or not
    if (switcher == True):
        doors.remove(player_initial_choice)
        doors.remove(host_door[0])
        player_final_choice = doors[0]
    else:
        doors.remove(host_door[0])
        player_final_choice = player_initial_choice

    #verifying the result
    if (player_final_choice == car_door):
        return 1
    else:
        return 0