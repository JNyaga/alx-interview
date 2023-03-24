#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    return len(best_sum(total, coins))


def best_sum(target_sum, numbers, memo={}):
    # check if target sum already exists in memoization dictionary
    if target_sum in memo:
        return memo[target_sum]
    # base cases
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None
    # iterate through numbers and recursively call function to find remainder combinations
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            # if combination is shorter than the current shortest, update it
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination
