class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0 
        j = len(height)-1
        heg,l,max = 0,0,0 
        Amount_of_water = 0
        while i < j:
            heg = height[min(height[i],height[j])]
            l=j-i
            print(heg,l)
            Amount_of_water = heg*l
            print(Amount_of_water)
            if Amount_of_water > max:
                max = Amount_of_water
            if height[i] < height[j]:
                i += 1
            if height[j] < height[i] or height[i] == height[j]:
                j -= 1
        return max
object1 = Solution()
print(object1.maxArea(height=[1,8,6,2,5,4,8,3,7]))
    