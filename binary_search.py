from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases
print('B I N A R Y  S E A R C H  A L G O R I T H M')
# Set of valid inputs
tests = []
# query occurs in the middle
tests.append({
    'input': {
        'cards': [15, 12, 10, 7, 3, 2, 1],
        'query': 10
    },
    'output': 2
})

# query is the first element
tests.append({
    'input': {
        'cards': [10, 9, 8, 7, 3, 2, 1],
        'query': 10
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [10, 9, 8, 7, -1, -2, -3],
        'query': -3
    },
    'output': 6
})

# cards array contains only 1 element
tests.append({
    'input': {
        'cards': [10],
        'query': 10
    },
    'output': 0
})

# cards array is empty
tests.append({
    'input': {
        'cards': [],
        'query': 10
    },
    'output': -1
})

# cards are repeated
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# cards are repeated
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 0
    },
    'output': 12
})

# Binary Search Algorithm
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            # check for repeated cards
            if  mid - 1 >= 0 and cards[mid - 1] == mid_number:
                hi = mid - 1
            else:
                return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1

# Large test
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2,
    },
    'output': 9999998
}

result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print("## Linear Search ##\nResult: {}\nPassed: {}\nExecution Time: {} ms\n\n".format(result, passed, runtime))

# compare with binary
result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print("## Binary Search ##\nResult: {}\nPassed: {}\nExecution Time: {} ms\n\n".format(result, passed, runtime))

# Execute Tests
evaluate_test_cases(locate_card, tests)
