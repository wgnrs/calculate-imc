class Imc:

    def __init__(self, height, weight, pacoca=None):
        self.height = height
        self.weight = weight
        self.pacoca = pacoca

    def calculate_imc(self):
        return round(self.weight / (self.height * 2), 2)
