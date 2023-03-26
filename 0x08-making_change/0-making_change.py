#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.

    Dyanimc Programmming Bottom Up Solution
    """
    if total <= 0:
        return 0
    
    table = [None] * (total + 1)
    table[0] = []

    for i in range(total+1):
        if table[i] is not None:
            for num in coins:
                combination = [*table[i] ,num]
                if(i+num<= total):
                    if (table[i + num] ==None or len(table[i + num]) > len(combination)):
                        table[i + num] = combination

    return len(table[total]) if table[total] is not None else -1
