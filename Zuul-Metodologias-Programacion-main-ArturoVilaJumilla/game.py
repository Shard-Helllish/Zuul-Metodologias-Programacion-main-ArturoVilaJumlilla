from typing import Text
from items import Item, Comestible#, tramportador
from player import Player
from stack import Stack, inverse
from room import Room
from parser_commands import Parser
from npc import Npc

class Game:
   
    def __init__(self):
        self.createRooms()
        self.parser = Parser()
        self.player = Player('jugador 1', 20)
        self.npc = Npc('Roberto', 30)

        self.stack = Stack()

    def createRooms(self):

        recividor = Room("Recividor, Primer habitacion e inicio de la aventura")        
        cocina = Room("Cosina, lugar magico, ideal para obtener proviciones")        
        baño = Room("Baño, te vendria bien, ya que apestas!")
        lebreria = Room("Libreria, la habitacion mas grande y misteriosa de la casa")
        dormitorio = Room("Dormitorio, ideal para descansar, si estas solo") 
        garage = Room("Garage, sin un vehiculo, solo unlugar vacio")
        salaDeJuegos = Room("Sala de juegos si no te controlas, nunca saldras")
        altillo = Room("Altillo, donde se esconden los libros prohibidos")
        calabozo = Room("Calabozo, condena para los que no estudian")
###
###
        recividor.setExits(None, baño, lebreria, cocina, None, None, None)
        baño.setExits(salaDeJuegos, None, None, recividor, None, None, None)
        cocina.setExits(None, recividor, garage, salaDeJuegos, None, None, None)
        dormitorio.setExits(None, None, salaDeJuegos, lebreria, None, None, None)
        garage.setExits(cocina, None, None, None, None, None, None)
        salaDeJuegos.setExits(dormitorio, cocina, None, baño, None, None, None)
        lebreria.setExits(recividor, None, None, None, altillo, calabozo, None)
        altillo.setExits(None, None, None, None, None, lebreria, None)
        calabozo.setExits(None, None, None, None, lebreria, None, None)
###
###
    #comestibles
        sandwich = Comestible("sandwich", "para recargar energias", 0.5, 0.5, "max_weight")
        fernecito = Comestible("fernecito", "bebida escencial", 0.6, 10, "max_weight" )

    #objetos
        florero = Item("florero", "siempre con flores frescas", 0.7)
        cuchillo = Item("cuchillo", "utencilio de cosina o arma", 0.2)
        jabon = Item("jabon", "usalo, no seas croto", 0.3)
        libro = Item("libro", "en el, los secreros de la casa", 0.5, )
        cuaderno = Item("cuaderno", "llevalo para encontrar la salida", 0.5)
        llave = Item("llave", "antigua como de calabozo", 0.1)
        linterna = Item("linterna", "necesaria en habitaciones oscuras de la casa", 1)
        auto = Item("auto", "camaro negro", 1000)
        tetris = Item("tetris", "horas de entretenimiento", 0.2)
        pelota = Item("pelota", "infaltable en una sala de juegos", 0.5)
        naipes = Item("naipes", "truco y retruco", 0.2)
        moneda = Item("moneda", "muy valiosa", 0.1)
        mosca = Item("mosca", "insecto intracendente, o no?", 0.01)
        candado = Item("candado", "con la forma especial de una Venus atrapa moscas", 1)
        #transportador = Item("transportador", "raro artefacto para este mundo", 1)
        antigua_llave = Item("antigua_llave", "raro artefacto para este mundo", 1)

    #muebles 
        mesa = Item("mesa", "muy antigua y pesada", 9, picked_up=False)
        silla = Item("Silla", "comoda como pocas", 6,picked_up=False )
        cama = Item("cama", "hazlo, descansa", 19, picked_up=False)
        baul = Item("baul", "nadie sabe como llego ahi ni que contiene", 80, picked_up=False )
        Banquito = Item("banquito", "muy incomodo, pero es el unico", 2,picked_up=False )
###
###
        recividor.setItem(florero)
        recividor.setItem(moneda)
        recividor.setItem(mosca)
        #recividor.setItem(transportador)
        recividor.setItem(antigua_llave)
        recividor.Npc

        cocina.setItem(cuchillo)
        cocina.setItem(sandwich)
        cocina.setItem(fernecito)
        cocina.setItem(mesa)
        cocina.setItem(silla)

        baño.setItem(jabon)
        baño.setItem(moneda)

        lebreria.setItem(mesa)
        lebreria.setItem(libro)
        lebreria.setItem(cuaderno)
        lebreria.setItem(llave)

        dormitorio.setItem(cama)
        dormitorio.setItem(moneda)

        garage.setItem(auto)
        garage.setItem(moneda)

        salaDeJuegos.setItem(mesa)
        salaDeJuegos.setItem(tetris)
        salaDeJuegos.setItem(pelota)
        salaDeJuegos.setItem(naipes)
        
        altillo.setItem(baul)
        altillo.setItem(moneda)
        altillo.setItem(candado)

        calabozo.setItem(linterna)
        calabozo.setItem(Banquito)

        self.currentRoom = recividor


        
        return

    def play(self):
        self.printWelcome()

        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Thank you for playing.  Good bye.")

    def printWelcome(self):
        print()
        print("Welcome to the World of Zuul!")
        print("World of Zuul is a new, incredibly boring adventure game.")
        print("Type 'help' if you need help.")
        print("")
        self.currentRoom.print_location_information()
        print()

    def processCommand(self, command):
        wantToQuit = False

        if(command.isUnknown()):
            print("I don't know what you mean...")
            return False

        commandWord = command.getCommandWord()
        if(commandWord == "help"):
            self.printHelp()
        elif(commandWord == "go"):
            self.goRoom(command)
        elif(commandWord == "quit"):
            wantToQuit = self.quit(command)
        elif(commandWord == "look"):
            self.look_items(command)
        elif(commandWord == "look"):
            self.look_npc(command) ####
        elif(commandWord == "bag"):
            self.bag_items(command)
        elif(commandWord == "back"):
            self.goBack(command)
        elif(commandWord == "take"):
            self.takeItem(command)
        elif(commandWord == "drop"):
            self.dropItem(command)
        elif(commandWord == "eat"):
            self.eatItem(command)
            #####################
        elif(commandWord == "talk"):
            self.talkItem(command)
        #elif(commandWord == "tp"):
         #   self.tramportadorItem(command)


#go|quit|help|look|back|take|drop|bag|eat|talk|tp

        return wantToQuit

    def printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the university.")
        print()
        print("Your command words are:")
        print("|go|quit|help|look|back|take|drop|bag|eat|talk|tp|")

    def goRoom(self, command):
        if(not command.hasSecondWord()):
            print("Go where?")
            return

        direction = command.getSecondWord()
        nextRoom = self.currentRoom.get_exit(direction)
       
        if(nextRoom is None):
            print("There is no door!")
        else:
            self.currentRoom = nextRoom
            self.currentRoom.print_location_information()
            self.stack.push(direction)
            print()
    
    def takeItem(self, command):
        if(not command.hasSecondWord()):
            print("Take what?")
            return

        item_name = command.getSecondWord()
        item = self.currentRoom.getItem(item_name)
       
        if(item is None):
            print("There is not item in the room with this name!")
        else:
            if(item.picked_up):
                if(self.player.can_picked_up_new_item(item.weight)):
                    self.player.setItem(item)
                else:
                    print('no puedes levantar tanto peso...')
                    self.currentRoom.setItem(item)
            else:
                print('ese item no puede ser levantado')
                self.currentRoom.setItem(item)

    def dropItem(self, command):
        if(not command.hasSecondWord()):
            print("Drop what?")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
       
        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            self.currentRoom.setItem(item)

    def eatItem(self, command):
        if(not command.hasSecondWord()):
            print("Eat what?")
            return

        item_name = command.getSecondWord()
        item = self.player.getItem(item_name)
       
        if(item is None):
            print("There is not item in the player bag with this name!")
        else:
            if(isinstance(item, Comestible)):
                response = item.comer(self.player)
                if(not response):
                    self.player.setItem(item)
            else:
                print('este item no es comestible')
                self.player.setItem(item)
###########################################
#  def TramportadorItem(self, command):
#        if(not command.hasSecondWord()):
#            print("talk what?")
#            return

#        npc_name = command.getSecondWord()
#        npc = self.player.getItem(npc_name)
       
#        if(npc is None):
#            print("There is not item in the player bag with this name!")
#        else:
#            if(isinstance(item, tramportador)):
#                response = item.(self.player)
#                if(not response):
#                    self.player.setItem(item)
#            else:
#                print('este item no es el tramportador')
#                self.player.setItem(item)
###########################################
    def look_items(self):
        self.currentRoom.print_items_information()

    def look_npc(self):
            self.currentRoom.print_npc_information()

    def bag_items(self):
        self.player.print_items_information()
    
    def goBack(self):
        direction = self.stack.pop()
        if(direction):
            nextRoom = self.currentRoom.get_exit(direction)
       
            if(nextRoom is None):
                print("There is no door! to go", direction)
                self.stack.push(inverse[direction])
            else:
                self.currentRoom = nextRoom
                self.currentRoom.print_location_information()
                print()
        else:
            print('you are in the initial position, can not go back')

    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True
g = Game()
g.play() 

