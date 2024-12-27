class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 9
        self.energy = 100
        self.happy = 70
        self.isAlive = True

    def info(self):
        print(f"Name = {self.name} Age = {self.age} Health =  {self.health} Energy = {self.energy} Happy = {self.happy}. ALive = {self.isAlive}")

    def checkAlive(self):
        if self.happy <= 0:
            self.isAlive = False
        elif self.energy <= 0:
            self.isAlive = False
        else:
            self.isAlive = True

    def sleep(self, hours):
        self.energy += hours * 10
        print(f"Zzz Zzz Zzzz. Repair energy = {hours * 10}")
        if self.energy > 100:
            diffrence = self.energy - 100
            self.energy = 100
            self.happy -= diffrence
        self.checkAlive()

    def play(self, hours):
        self.energy -= hours * 10
        self.happy += hours * 10
        print(f"Кіт грається ха-ха-ха мяв мяв")
        self.checkAlive()

    def feed(self, num):
        self.energy += num * 8
        self.happy += num * 2
        print(f"Ням ням. Котик з'їв аж {num} миски корму.")
        if self.energy > 130:
            self.energy = 100
            print("Котик обжерся і кікнувся:(")
            self.health -= 1
        self.checkAlive()

    def buy_toys(self, num_of_toys):
        if num_of_toys <= 0:
            print("Котик плаче.")
        else:
            print(f"Котик отримав {num_of_toys} іграшок!")
            self.happy += num_of_toys * 5
            self.energy -= num_of_toys * 2
            if self.energy < 0:
                self.energy = 0
            self.checkAlive()


cat1 = Cat("Tom")
print("Лaсково просимо в нашу гру")
while(cat1.isAlive):
    anw = input("Введіть команду ")
    if (anw.lower() == "play"):
        hours = int(input("Скільки годин кіт буде грати? "))
        cat1.play(hours)
    elif(anw.lower() == "sleep"):
        hours = int(input("Скільки годин кіт буде спати? "))
        cat1.sleep(hours)
    elif anw == "feed":
        num = int(input("Скільки корму дати коту? "))
        cat1.feed(num)
    elif anw == "buy_toy":
        num_of_toys = int(input("Скільки іграшок купити? "))
        cat1.buy_toys(num_of_toys)

    cat1.info()

print("Вибач, але кіт попав в котячий рай :(")