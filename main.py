import random
import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.total_damage_dealt = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack(self, other_player):
        damage = random.randint(10, 20)
        other_player.take_damage(damage)
        self.total_damage_dealt += damage
        print(f"{self.name} attacked {other_player.name} for {damage} damage!")

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s Inventory: {', '.join(self.inventory)}")
        else:
            print(f"{self.name}'s Inventory is empty.")

    def use_health_potion(self):
        if "Health Potion" in self.inventory:
            self.health += random.randint(10, 20)
            print(f"{self.name} used a Health Potion and restored health.")
            self.inventory.remove("Health Potion")
        else:
            print(f"{self.name} doesn't have a Health Potion in their inventory.")

    def use_ammunition(self, other_player):
        if "Ammunition" in self.inventory:
            damage_boost = random.randint(5, 10)
            other_player.take_damage(damage_boost)
            self.total_damage_dealt += damage_boost
            print(f"{self.name} used Ammunition to deal extra damage to {other_player.name}.")
            self.inventory.remove("Ammunition")
        else:
            print(f"{self.name} doesn't have Ammunition in their inventory.")

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def print_stats(self):
        print("\n--- Game Stats ---")
        print(f"{self.player1.name} Health: {self.player1.health}")
        print(f"{self.player2.name} Health: {self.player2.health}")
        print(f"Total Damage Dealt by {self.player1.name}: {self.player1.total_damage_dealt}")
        print(f"Total Damage Dealt by {self.player2.name}: {self.player2.total_damage_dealt}")

def main():
    # Create players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Create the game
    game = Game(player1, player2)

    # Game loop
    round_number = 1
    while player1.health > 0 and player2.health > 0:
        print(f"\n--- Round {round_number} ---")
        player1.attack(player2)
        player2.attack(player1)

        # Players interact with inventory
        player1.pick_up_item("Health Potion")
        player2.pick_up_item("Ammunition")

        # Players communicate
        print("\n--- Communication ---")
        player1.show_inventory()
        player2.show_inventory()

        # Players use items
        print("\n--- Use Items ---")
        player1.use_health_potion()
        player2.use_ammunition(player1)

        round_number += 1

    print("\n--- Game Over ---")
    if player1.health <= 0:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

    # Print final game stats
    game.print_stats()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
