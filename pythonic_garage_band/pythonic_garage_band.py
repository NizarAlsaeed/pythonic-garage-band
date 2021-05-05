Musician.members=[]
class Musician:
    def __init__(self,name:str):
        self.name = name
    members.append(self)
    
    def get_instrument(self):
        return ''

    def play_solo(self):
        return ''
    
    def __repr__(self):
        return 'Musician('+ self.name + ')'

    
    def __str__(self,role):
        return f'A Musician class.\nRole: {role}'

class Band(Musician):
    def __init__(self,name:str,members:list):
        self.name =name
        self.members = super().members

    def play_solos ():


    def __repr__(self):
        return 'Band('+ self.name +','+ self.members ')'
    
    def __str__(self,role):
        print(f'A Musician class.\nRole: {role}')

    def to_list():


Guitarist = Musician()
Bassist = Musician
Drummer = Musician