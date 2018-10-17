class TestingObject:
    var = "Hello!"

    def function(self):
        print("Hello I'm just a function")

class Vehicle:
    type = "Motorcycle"
    cupholders = False
    numSeats = 1
    engine = True

    def getType(self):
        return self.type

    def setType(self,name):
        self.type = name

    def getSeats(self):
        return self.numSeats

    def setSeats(self,num):
        self.numSeats = num

class Pokemon:
    name = ""
    type = ""
    rarity=""
    feet = 0
    defence = 0
    attack = 0
    health = 100

    def setName(self , name):
        self.name =name

    def setType(self,type):
        self.type =type

    def takeDamage(self,dmg):
        self.health = self.health - dmg

    def setRarity(self,rarity):
        self.rarity = rarity

    def setDefence(self,defence):
        self.defence = defence

    def setAttack(self,attack):
        self.attack = attack

    def setHealth(self,health):
        self.health = health

    def getStatus(self):
        print("************"+self.name+"************")
        print("Type :"+self.type)
        print("rarity"+self.rarity)
        #print("defence"+self.defence)
        #print("attack"+self.attack)
        #print("health"+self.health)



#myObject = TestingObject()
#
#print( myObject.var)

poke1 = Pokemon()
poke1.setName("Erickomn")
poke1.setRarity("Mythical")
poke1.setType("Fire")
poke1.getStatus()

#vehicle1 = Vehicle()

#vehicle1.setSeats(45)

#vehicle1.setType(input())

#print( vehicle1.getSeats() )
