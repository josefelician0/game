import random
class Character:
    def __init__(self, name, hp, force, defense):
        self.name = name
        self.hp = hp
        self.force = force
        self.defense = defense
        
    def attributes(self):
        print(f"{self.name}:")
        print("·Vida:", self.hp)
        print("·Daño:", self.force)
        print("·Defensa:", self.defense)

    def its_alive(self):
        return self.hp > 0

    def die(self):
        self.hp = 0
        print(self.name, "ha muerto")

    def damage(self, enemy):
        return self.force - enemy.defense
    
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.hp = enemy.hp - damage
        print(self.name, "ha realizado", damage, "puntos de daño a", enemy.name)
        if enemy.its_alive():
            print("Vida de", enemy.name, "es", enemy.hp)
        else:
            enemy.die()

    def dodge(self):
        aleatorio = random.randint(1, 2)
        if aleatorio == 1:
            print("Has esquivado la lanza de Odín")
            return True
        else:
            print("No has podido esquivar la embestida de Odín")
            return False

class Wizard(Character):
    def __init__(self, name, hp, force, defense, wisdom):
        super().__init__(name, hp, force, defense)
        self.wisdom = wisdom
    
    def attributes(self):
        super().attributes()
        print("·Sabiduría:", self.wisdom)

    def damage(self, enemy):
        return self.force+self.wisdom - enemy.defense
              
class Berserker(Character):
    def __init__(self,name,hp, force, defense, fury):
        super().__init__(name, hp, force, defense)
        self.fury = fury

    def attributes(self):
        super().attributes()
        print("·Furia:", self.fury)
    
    def damage(self, enemy):
        return self.force+self.fury - enemy.defense
              
class Assassin(Character):
    def __init__(self,name, hp, force, defense, energy):
        super().__init__(name, hp, force, defense)
        self.energy = energy

    def attributes(self):
        super().attributes()
        print("·Energía:", self.energy)

    def damage(self, enemy):
        return self.force+self.energy - enemy.defense
              
class Boss(Character):
    def __init__(self,name, hp, force, defense):
        super().__init__(name, hp, force, defense)
    
    def boss_attack(self, enemy):
        damage = random.randint(30, 60)
        enemy.hp = enemy.hp - damage
        print(self.name, "ha realizado", damage, "puntos de daño a", enemy.name)
        if enemy.its_alive():
            print("Vida de", enemy.name, "es", enemy.hp)
        else:
            enemy.die()
            
def choose_class():
    contador = 0
    while True:
        print("Bienvenido al Gran Coliseo. Elige tu clase:")
        print("1. Mago")
        print("2. Vikingo")
        print("3. Asesino")
        choice = int(input("Escribe el número de la clase que quieres elegir: "))

        if choice == 1:
            name = input("Escribe el nombre de tu personaje: ")
            print(f"¡Bienvenido, {name}! ¡Aprovecha tu sabiduría y magia para dezatar todo tu poder!")
            return Wizard(name, 180, 30, 200, 350)
        elif choice == 2:
            name = input("Escribe el nombre de tu personaje: ")
            print(f"¡Bienvenido, {name}! ¡Usa tu furia para aplastar a tus oponentes!")
            return Berserker(name, 250, 50, 150, 250)
        elif choice == 3:
            name = input("Escribe el nombre de tu personaje: ")
            print(f"¡Bienvenido, {name}! ¡Utiliza tu astucia y sigilo para derrotar a tus victimas!")
            return Assassin(name, 160, 35, 170, 300)
        else:
            print("Opción inválida, intentalo nuevamente")
            contador += 1

def choose_action():
    contador = 0
    while True:
        if contador == 3:
            print("Has superado el límite de intentos. Turno finalizado.")
            return
        
        print("¿Qué quieres hacer?")
        print("1. Atacar")
        print("2. Esquivar")
        option = int(input())

        if option == 1:
            return "atacar"
        elif option == 2:
            return "esquivar"
        else:
            print("Opción inválida")
            contador += 1
    
def combat(player, boss_1):
    round = 1
    while player.its_alive() and boss_1.its_alive():
        print("\nRonda", round)
        print(f">>> Turno de {player.name} <<<")
        act = choose_action()
        if act == "atacar":
            player.attack(boss_1)
            if boss_1.its_alive():
                print(f">>> Turno de {boss_1.name} <<<")
                boss_1.boss_attack(player)
        elif act == "esquivar":
            dodged = player.dodge()
            if dodged:
                print("Odín retrocede")
            else:
                if boss_1.its_alive():
                    print(f">>> Turno de {boss_1.name} <<<")
                    boss_1.boss_attack(player)
        round = round + 1
    #Reseteamos para el próximo turno
        dodged = False