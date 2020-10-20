class Stack():
    
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
                
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        if self.items == []:
            return True
        
                    
    def peek(self):
        if not self.items == []:
            return self.items[-1]
            
        
                    
               
    def visual(self):
        return self.items
    
s = Stack()


Input = "{[()]}"

def check(char):

    for character in Input:
        
            
        
        if character == "(" or character == "[" or character == "{":
            s.push(character)
        
        else:
            if s.isEmpty():
                print ("Not Balanced",s.visual())
                return False
            
            if (character == ")" and s.peek() == "(") or (character == "]" and s.peek() == "[") or (character == "}" and s.peek() == "{") :
                s.pop()
            else:
                print ("Not Balanced",s.visual())
                return False
                
            
    
            
    if (s.visual()) == []:
        
        print("Balanced",s.visual())
    
    else:
        print ("Not Balanced",s.visual())
    
    
        

check(Input)
    
            


    
    
        
        
    