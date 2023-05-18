#!/usr/bin/python3
"""Change making module. finding the smallest possible combination of a list value to make total
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins which is a list of integers of different values.
    """
    if total <= 0:
        return 0
    remainder = total
    count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    numb = len(coins)
    while remainder > 0:
        if coin_index >= numb:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            count += 1
        else:
            coin_index += 1
    return count
