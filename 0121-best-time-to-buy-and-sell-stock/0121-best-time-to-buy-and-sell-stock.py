class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_profit = 0
        left , right = 0 , 1
        while right < len(prices):
            if prices[left]<prices[right]:
                curr_profit = prices[right] - prices[left]
                profit = max(curr_profit,profit)
            else:
                left = right
            right = right + 1
        return profit