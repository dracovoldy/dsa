# import math
# print(math.ceil(54.1))

## Set of valid inputs
tests = []
## query occurs in the middle
tests.append({
    'input': {
            'cards': [15, 12, 10, 7, 3, 2, 1],
            'query': 10 
        }, 
        'output': 2
})

## query is the first element
tests.append({
    'input': {
            'cards': [10, 9, 8, 7, 3, 2, 1],
            'query': 10 
        }, 
        'output': 0
})

## query is the last element
tests.append({
    'input': {
            'cards': [10, 9, 8, 7, -1, -2, -3],
            'query': -3 
        }, 
        'output': 6
})

## cards array contains only 1 element
tests.append({
    'input': {
            'cards': [10],
            'query': 10 
        }, 
        'output': 0
})

## cards array is empty
tests.append({
    'input': {
            'cards': [],
            'query': 10 
        }, 
        'output': -1
})

# Brute Force Algorithm

def locate_card(cards, query):
    position = 0

    if len(cards) <= 0:
        return -1

    # loop
    while True:

        # check if card at position matches query
        if cards[position] == query:
            return position
        
        position = position + 1

        # reached end of cards
        if position == len(cards):
            # number not found
            return -1

## Execute Tests
test_pos = 0
while test_pos < len(tests):
    
    print('TEST ', test_pos + 1, ': ', tests[test_pos])
    result = locate_card(tests[test_pos]['input']['cards'], tests[test_pos]['input']['query'])

    if result == tests[test_pos]['output']:
        print('PASSED, result: ', result)
        
    elif result == -1:
        print('FAILED, result: ', result)
    test_pos = test_pos + 1
