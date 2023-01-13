from GameOk import Character, Wizard, Berserker, Assassin, Boss, choose_class, choose_action, combat
def main():
    player = choose_class()
    boss_1 = Boss("Odín", 350, 50, 250)

    player.attributes()
    boss_1.attributes()

    combat(player, boss_1)

    if not player.its_alive():
        print("\nHa ganado", boss_1.name)
    elif not boss_1.its_alive():
        print("\nHa ganado", player.name)
        print("\nFelicidades, FIN.")
        print("CREDITOS:")
        print("José Peña\nJean Moscoso\nGiovanni González")

if __name__ == "__main__":
    main()