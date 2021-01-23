class Guitar:
    def __init__(self, guitar_string):
        self.string = guitar_string


class String:
    def __init__(self):
        pass


guitar_strings = String()
guitar = Guitar(String)


class Laptop:
    def __init__(self):
        self.graphics_card = GraphicsCard("4 GB")
        self.cpu = CPU("2.5 GHz")

    def __str__(self):
        return f"Laptop's Graphic card memory is {self.graphics_card}, CPU frequency is {self.cpu}"


class GraphicsCard:
    def __init__(self, memory):
        self.memory = memory

    def __str__(self):
        return self.memory


class CPU:
    def __init__(self, frequency):
        self.frequency = frequency

    def __str__(self):
        return self.frequency


laptop = Laptop()
