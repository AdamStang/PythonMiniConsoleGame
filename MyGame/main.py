import random
import time


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Warrior(Person):
    def __init__(self, name, level, experience, health, attack, armor, defense, money):
        super().__init__(name)
        self.level = level
        self.experience = experience
        self.maxExp = 1000
        self.health = health
        self.attack = attack
        self.armor = armor
        self.defense = defense
        self.money = money

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def get_max_exp(self):
        return self.maxExp

    def set_max_exp(self, max_exp):
        self.maxExp = max_exp

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack

    def get_armor(self):
        return self.armor

    def set_armor(self, armor):
        self.armor = armor

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money


class Barbar(Warrior):
    def __init__(self):
        self.name = "Barbarian"
        self.level = 1
        self.experience = 0
        self.maxExp = 500
        self.health = 200
        self.attack = 15
        self.armor = 1
        self.defense = 1
        self.price = 300

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


def countdown(t):
    while t:
        m, secs = divmod(t, 60)
        tf = '{:02d}:{:02d}'.format(m, secs)
        print(tf, end="")
        time.sleep(1)
        print(tf, end="\r")
        t -= 1


def menu():
    name = input("Type your name: ")
    level = 1
    exp = 0
    health = 250
    attack = 25
    armor = 1
    defense = 1
    money = 500
    war = Warrior(name, level, exp, health, attack, armor, defense, money)
    army_list = list()
    army = dict()
    consider = False
    wars = 300 + (level * 50)
    training = 200 + (level * 50)
    a = 0
    while a < 6:
        army = dict()
        for v in army_list:
            if v.get_name() in army:
                army[v.get_name()] += 1
            else:
                army[v.get_name()] = 1
        print(
              "-------------------- \n"
              "[1] Go to Attack - Gain {} gold \n"
              "[2] Train - Pay {} Gold \n"
              "[3] Buy Soldiers \n"
              "[4] My Stats \n"
              "[5] My Army \n"
              "[6] Exit \n"
              "--------------------".format(wars, training))
        a = int(input("Command: "))
        if a == 1:
            exp += random.randint(200 + (50 * war.get_level()), 600 + (50 * war.get_level()))
            war.set_experience(exp)
            war.set_money(war.get_money() + wars)
            countdown(100 * war.get_level())
        if a == 2:
            if war.get_money() >= training:
                exp += (300 + (50 * war.get_level()))
                war.set_experience(exp)
                war.set_money(war.get_money() - training)
                countdown(25 * war.get_level())
        if a == 3:
            consider = False
            print("[1] Barbarian"
                  "[2] Archer")
            b = input("Command: ")
            while not consider:
                q = input("Quantity: ")
                if (int(q) * Barbar().get_price()) > war.get_money():
                    consider = False
                else:
                    consider = True
            for i in range(int(q)):
                army_list.append(Barbar())
                war.set_money(war.get_money() - Barbar().get_price())
        if a == 4:
            print("Name: {} \n"
                  "Money: {} \n"
                  "Level: {} \n"
                  "Exp: {} \n"
                  "Max Exp: {} \n"
                  "Health: {} \n"
                  "Attack: {} \n"
                  "Armor: {} \n"
                  "Defense: {} \n".format(war.get_name(), war.get_money(),  war.get_level(), war.get_experience(),
                                          war.get_max_exp(), war.get_health(), war.get_attack(), war.get_armor(),
                                          war.get_defense()))
        if a == 5:
            for key in army:
                print(key, ': ', army[key])

        if war.get_experience() > war.get_max_exp():
            exp -= war.get_max_exp()
            war.set_experience(exp)
            war.set_max_exp(war.get_max_exp() + 1000)
            level += 1
            war.set_level(level)
            attack += 5
            war.set_attack(attack)
            health += 50
            war.set_health(health)
            armor += 0.1
            war.set_armor(armor)
            defense += 1
            war.set_defense(defense)


menu()
