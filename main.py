from time import time


def find_coins_greedy(value):
    coins = [1, 2, 5, 10, 25, 50]
    sorted_coins = sorted(coins, reverse=True)

    little_change = {}

    while value > 0:
        for coin in sorted_coins:
            if value >= coin:
                value -= coin

                if not coin in little_change:
                    little_change[coin] = 1
                else:
                    little_change[coin] += 1

    return little_change


def find_min_coins(value):
    coins = [1, 2, 5, 10, 25, 50]

    dp = [float("inf")] * (value + 1)
    dp[0] = 0

    used_coin = [-1] * (value + 1)

    for coin in coins:
        for i in range(coin, value + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coin[i] = coin

    if dp[value] == float("inf"):
        return {}

    result = {}

    while value > 0:
        coin = used_coin[value]

        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        value -= coin

    return result


def compare_methods(value):

    start = time()
    greedy_result = find_coins_greedy(value)
    greedy_time = time() - start

    start = time()
    dp_result = find_min_coins(value)
    dp_time = time() - start

    return greedy_result, greedy_time, dp_result, dp_time


if __name__ == "__main__":

    value = 113
    greedy_result, greedy_time, dp_result, dp_time = compare_methods(value)

    print(
        f"Greedy_method: \n\tresult >> {greedy_result}, \n\ttime >> {greedy_time:.8f} сек")
    print(
        f"DP_method: \n\tresult >> {dp_result}, \n\ttime >> {dp_time:.8f} сек")
