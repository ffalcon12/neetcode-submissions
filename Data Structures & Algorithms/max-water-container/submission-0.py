class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #1-  we want right as least as high as highest left
        # 2- max distance keeping 1 in mind

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            dist = r - l 
            area = min(heights[l], heights[r]) * dist
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
