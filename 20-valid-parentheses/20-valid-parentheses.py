class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]==")":
                if not stack or  "(" not in stack:
                    return False
                                                  
                if stack[-1]=="(":
                    stack.pop()
                                 
            elif s[i]=="]":
                if not stack or   "[" not in stack:
                    return False
                if stack[-1]=="[":
                    stack.pop()
            elif s[i]=="}":
                if not stack or  "{" not in stack:
                    return False
                                    
                if stack[-1]=="{" :
                    stack.pop()
            else:
                stack.append(s[i])
            
    
        if len(stack)==0:
            return True
            
        
                            
                                 
                    
                    
                            
                
            
            
                        
        