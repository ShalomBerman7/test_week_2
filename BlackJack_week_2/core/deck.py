from random import randint
def build_standard_deck():
    list_deck = []
    for i in ['S','D','C','H']:
        for j in range(2, 11):
            list_deck.append({'rank': str(j), 'suite': i})
        list_deck.append({'rank': 'J', 'suite': i})
        list_deck.append({'rank': 'Q', 'suite': i})
        list_deck.append({'rank': 'K', 'suite': i})
        list_deck.append({'rank': 'A', 'suite': i})
    return list_deck
print(build_standard_deck())


def shuffle_by_suit(deck: list[dict], swaps: int = 5000):
    for i in range(swaps):
        i = randint(0,len(deck) -1)
        j = randint(0,len(deck) -1)
        ######### צריך להמשיך
        while deck[i] == deck[j]:
            j = randint(0, len(deck) - 1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

print(shuffle_by_suit(build_standard_deck()))
