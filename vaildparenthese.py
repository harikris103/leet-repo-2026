class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            
            if char in mapping:
               
                top_element = stack.pop() if stack else '#'
                
               
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        
        return len(stack) == 0

        
