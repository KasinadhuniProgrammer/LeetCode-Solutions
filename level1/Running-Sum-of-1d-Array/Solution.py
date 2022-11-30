#My solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: 
            return nums 
        else:
            s = []
            for i in range(len(nums)):
                s.append(sum(nums[:i+1]))
        return s 
     
#Success
