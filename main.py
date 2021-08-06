# selector (TEST)

import random

# library of friends to FaceTime

friends = [
    'Dave',
    'Elias',
    'Laura',
    'Bella',
    'Max',
    'Anna',
    'Lex',
    'Amy',
    'Nadya'
]

selected = random.choice(friends) # randomly choose a friend

print('Who should I facetime today?')
print(selected)