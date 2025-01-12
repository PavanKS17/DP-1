#Similar to coin change, we need to use same dp table but use sum instead of min to store the number of ways of solving the problems, return the final element
#TC: O(n*m)
#SC: O(n*m)
#Yes, this worked in leetcode
#Same issue as coin change when used recursion

def change(self, amount: int, coins: List[int]) -> int:
    if len(coins) == 0:
        return 0
    dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
    for i in range(len(coins) + 1):
        dp[i][0] = 1
    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j < coins[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
    return dp[len(coins)][amount]