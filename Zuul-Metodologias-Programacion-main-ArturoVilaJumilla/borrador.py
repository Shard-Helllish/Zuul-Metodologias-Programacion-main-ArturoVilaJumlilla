class tramportador(Item):
            
    def __init__(self, name, description, weight, incremet, atribute, picked_up=True):
        super().__init__(name, description, weight, picked_up)
        self.increment = incremet
        self.atribute = atribute
    
    def comer(self, player):
        if(self.atribute in player.__dict__):
            print('current', self.atribute, player.__dict__[self.atribute])
            print('el jugador se ha comido', self.name)
            player.__dict__[self.atribute] += self.increment
            print('new', self.atribute, player.__dict__[self.atribute])
            return True
        else:
            print('el jugador no tiene atributo', self.atribute)
            return False

            ##########################################
#class tramportador(Item):
    
        def __init__(self, name, description, weight, incremet, atribute, picked_up=True):
            super().__init__(name, description, weight, picked_up)
        self.increment = incremet
        self.atribute = atribute
    
        def comer(self, player):
         if(self.atribute in player.__dict__):
            print('current', self.atribute, player.__dict__[self.atribute])
            print('el jugador se ha comido', self.name)
            player.__dict__[self.atribute] += self.increment
            print('new', self.atribute, player.__dict__[self.atribute])
            return True
         else:
            print('el jugador no tiene atributo', self.atribute)
            return False