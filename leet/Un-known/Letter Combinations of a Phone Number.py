class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_options = {'2' : ['a','b','c'] , '3' : ['d','e', 'f'] , '4' : ['g', 'h', 'i'] , '5' : ['j','k','l'] ,
                          '6' : ['m', 'n', 'o'] , '7' : ['p','q','r','s'] , '8' : ['t','u','v'] , '9' : ['w','x','y','z']}
        def dfs(compination_so_far,digits):
            if len(digits) == 0:
                answers.append(compination_so_far)
            else:
                for phone_latter in digits_options[digits[0]]:
                    dfs(compination_so_far + phone_latter,digits[1:])

        answers = []
        if digits:
            dfs("",digits)
        return answers

print(Solution.letterCombinations(Solution,"245"))




