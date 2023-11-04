#     1 Завдання
class life:
    def __init__(self):
        self.mood = 0
        self.messiness = 0
        self.car_condition = 100
        self.money = 1000

    def chill(self):
        self.mood += 10
        self.messiness += 5

    def clean_home(self):
        self.mood -= 5
        self.messiness = 0

    def to_repair(self):
        self.car_condition += 100
        self.money -= 50




