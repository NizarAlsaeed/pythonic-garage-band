
class Musician:
    members = []
    def __init__(self,name:str):
        self.name = name
        self.members.append(self)
    def get_instrument(self):
        pass

    def play_solo(self):
        pass
    
    def __repr__(self):
        return 'Musician('+ self.name + ')'

    
    def __str__(self):
        return f'My name is {self.name} and I play guitar'


class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return 'face melting guitar solo'


class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return 'rattle boom crash'

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f'My name is {self.name} and I play bass'
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'


class Band:
    instances=[]
    def __init__(self,name:str,members:list):
        self.name = name
        self.members = members
        Band.instances.append(self)
    def play_solos (self):
        return [instance.play_solo() for instance in self.members]

    def __repr__(self):
        return 'Band('+ self.name +','+ self.members+ ')'
    
    def __str__(self):
        print(f'A Band class.')

    @classmethod
    def to_list(cls):
        return cls.instances

print(Band.to_list())
