class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        current_sum = 0
        ans = [None]*2
        j = len(numbers)-1
        #for i in range(0,len(numbers),1):
        i = 0
        while i < len(numbers): 
            current_sum = numbers[i] + numbers[j]
            print(numbers[i],numbers[j],current_sum,target)
            if current_sum == target:
                print(i,j)
                ans[1] = j+1
                ans[0] = i+1
                return ans[0],ans[1]
                #the return statement automatically breaks the code 
            elif current_sum > target:
                j -= 1
            else:
                i +=1
solution =  Solution()
print(solution.twoSum(numbers=[2,7,11,15],target=9))
print(solution.twoSum([2,3,4],6))
print(solution.twoSum([-1,0],-1))