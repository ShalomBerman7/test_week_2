# import deck
import re
from core.deck import shuffle_by_suit, build_standard_deck


def calculate_hand_value(hand: list[dict]):
    print(hand)
    sumlis = []
    if hand[0]['rank'] == 'J' or hand[0]['rank'] == 'Q' or hand[0]['rank'] == 'K':
        sumlis.append(int(10))
    elif hand[0]['rank'] == 'A':
        sumlis.append(int(1))
    else:
        sumlis.append(int(hand[0]['rank']))
    if hand[1]['rank'] == 'J' or hand[0]['rank'] == 'Q' or hand[0]['rank'] == 'K':
        sumlis.append(int(10))
    elif hand[1]['rank'] == 'A':
        sumlis.append(int(1))
    else:
        sumlis.append(int(hand[1]['rank']))
    print(sum(sumlis))
    return sum(sumlis)


def deal_two_each(deck: list[dict], player: dict, dealer: dict):
    p_list = []
    d_list = []
    for i in range(2):
        p = deck.pop(0)
        p_list.append(p)
        d = deck.pop(0)
        d_list.append(d)
    calculate_hand_value(p_list)
    calculate_hand_value(d_list)
dth = deal_two_each(shuffle_by_suit(build_standard_deck()),{},{})


def dealer_play(deck: list[dict], dealer: dict):
    pass


def ask_player_action():
    cher = input('enter H/S')
    while not re.match("^[H,S]", cher) or len(cher) != 1:
        cher = input('enter H/S')
    return cher
