class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

mista = person('Mista', 17)
arlon = person('Arlon', 43)


print(mista.name)
print(mista.age)

class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

dog = animal('Haski','bark bark')
cat = animal('Cat','meow meow')
cow = animal('cow','moo moo')
