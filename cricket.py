import random

choice = [1, 2, 3, 4, 6, 'out', 'wide ball', 'no ball']

runs = 0
balls = 0
wide_balls = 0
no_ball = 0


player = input('Enter The Player Name:').title()

while(True):
    cricket = input('Press Enter For Hit The Ball')
    output = random.choice(choice)
    if balls == 6:
        break
    if output == 1:
        runs = runs + 1
        balls = balls + 1
        print(f'Its {output}')
    elif output == 2:
        runs = runs + 2
        balls = balls + 1
        print(f'Its {output}')
    elif output == 3:
        runs = runs + 3
        balls = balls + 1
        print(f'Its {output}')
    elif output == 4:
        runs = runs + 4
        balls = balls + 1
        print(f'Its {output}')
    elif output == 6:
        runs = runs + 6
        balls = balls + 1
        print(f'Its {output}')
    elif output == 'out':
        runs = runs + 0
        balls = balls + 1
        print(f'Its Out ')
        break
    elif output == 'wide ball':
        runs = runs + 1
        wide_balls = wide_balls + 1
        print(f'Wide Ball ')
    elif output == 'no ball':
        noball = random.randint(1,6)
        print(f"{noball} and Its No Ball, FREE HIT!")
        runs = runs + noball
        no_ball = no_ball + 1


print(f'{player} scored {runs} runs in {balls + no_ball + wide_balls} balls ')