from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        
        half = []
        middle = ''
        
        for ch in sorted(count.keys()):
            freq = count[ch]
            if freq % 2 == 1:
                middle = ch
            half.append(ch * (freq // 2))
        
        half_str = ''.join(half)
        return half_str + middle + half_str[::-1]