class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        for i in range(len(s)-1):
            j = i + 1
            while(j<len(s)):
                if(s[i]!=s[j]):
                    j = j + 1
                else:
                    c = len(s[i:j])
                    m = max(m, c)
                    break
        return m

s = Solution()
print(s.lengthOfLongestSubstring("abcmbcdpzm"))