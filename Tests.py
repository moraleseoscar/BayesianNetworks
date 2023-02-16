import itertools

letters  = {'E': {'BC': 0.15, 'B-C': 0, '-BC': 0, '-B-C': 0}, 'D': {'B': 0, '-B': 0}, 'C': {'A': 0, '-A': 0}, 'B': {'A': 0, '-A': 0}, 'A': 0}

print(type(letters.get('A')) == int)