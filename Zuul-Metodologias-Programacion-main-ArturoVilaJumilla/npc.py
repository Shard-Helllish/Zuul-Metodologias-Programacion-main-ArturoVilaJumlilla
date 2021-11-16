
class Npc():

    def __init__(self, max_weight, talk):
        
        self.max_weight = max_weight
        self.items = {None}
        self.strength = 1
        self.defese = 1
        self.talk = talk #('Nesesito la antigua llave') 


    def getItem(self, item):
        if(item in self.items):
            return self.items.pop(item)
        return None