# 1395. Count Number of Teams

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        ans, n = 0, len(rating)
        for i, b in enumerate(rating):
            l = sum(a < b for a in rating[:i])
            r = sum(c > b for c in rating[i + 1 :])
            ans += l * r
            ans += (i - l) * (n - i - 1 - r)
        return ans