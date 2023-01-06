# https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1, n+1):
            if i%5 == 0 and i%3 == 0:
                a.append("FizzBuzz")
            elif i%5 == 0:
                a.append("Buzz")   
            elif i%3 == 0:
                a.append("Fizz")
            else:
                a.append(str(i))
                
        return a
