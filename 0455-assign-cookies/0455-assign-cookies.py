class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        content_children = 0
        i = j = 0
        while (i < len(g)) and (j < len(s)):
            if sorted_g[i] <= sorted_s[j]:
                content_children += 1
                i += 1
                j += 1
            else:
                j += 1
        return content_children

        