# https://leetcode.com/problems/power-of-three/submissions/894973352/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(True):
            if(n==1):
                return True
            if(n==0):
                return False
            if(n%3==0):
                n=n/3
                if(n==1):
                    return True
            else:
                return False
