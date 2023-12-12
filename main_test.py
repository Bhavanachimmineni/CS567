import unittest
from unittest.mock import patch, MagicMock

from main import Player, Game 

class TestPlayer(unittest.TestCase):
    def test_take_damage(self):
        player = Player("TestPlayer")
        player.take_damage(30)
        self.assertEqual(player.health, 70)

    def test_attack(self):
        player1 = Player("Attacker")
        player2 = Player("Defender")
        player1.attack(player2)
        self.assertGreater(player2.health, 0)
        self.assertGreater(player1.total_damage_dealt, 0)

    def test_pick_up_item(self):
        player = Player("TestPlayer")
        player.pick_up_item("Health Potion")
        self.assertIn("Health Potion", player.inventory)

    def test_show_inventory(self):
        player = Player("TestPlayer")
        player.pick_up_item("Health Potion")
        player.pick_up_item("Ammunition")
        with patch('sys.stdout', new_callable=MagicMock) as mock_stdout:
            player.show_inventory()
            expected_output = "TestPlayer's Inventory: Health Potion, Ammunition."
            mock_stdout.assert_called_with(expected_output)

    def test_use_health_potion(self):
        player1 = Player("User")
        player2 = Player("OtherPlayer")
        player1.pick_up_item("Health Potion")
        initial_health = player1.health
        player1.use_health_potion()
        self.assertGreater(player1.health, initial_health)

    def test_use_ammunition(self):
        player1 = Player("User")
        player2 = Player("OtherPlayer")
        player1.pick_up_item("Ammunition")
        initial_health = player2.health
        player1.use_ammunition(player2)
        self.assertLess(player2.health, initial_health)

    def test_use_invalid_item(self):
        player = Player("TestPlayer")
        with patch('sys.stdout', new_callable=MagicMock) as mock_stdout:
            player.use_health_potion()  # Corrected to use_health_potion
            expected_output = "TestPlayer doesn't have a Health Potion in their inventory."
            mock_stdout.assert_called_with(expected_output)

    def test_use_ammunition_no_inventory(self):
        player1 = Player("User")
        player2 = Player("OtherPlayer")
        initial_health = player2.health
        player1.use_ammunition(player2)
        self.assertEqual(player2.health, initial_health)

    def test_use_health_potion_no_inventory(self):
        player1 = Player("User")
        initial_health = player1.health
        player1.use_health_potion()
        self.assertEqual(player1.health, initial_health)

    def test_use_ammunition_other_player_no_damage(self):
        player1 = Player("User")
        player2 = Player("OtherPlayer")
        player1.pick_up_item("Ammunition")
        initial_health = player2.health
        player1.use_ammunition(player2)
        self.assertEqual(player2.health, initial_health)

    def test_use_health_potion_invalid_item(self):
        player1 = Player("User")
        player1.pick_up_item("InvalidItem")
        initial_health = player1.health
        player1.use_health_potion()
        self.assertEqual(player1.health, initial_health)

    def test_take_damage_player_defeated(self):
        player = Player("TestPlayer")
        with patch('sys.stdout', new_callable=MagicMock) as mock_stdout:
            player.take_damage(150)
            expected_output = "TestPlayer has been defeated!"
            mock_stdout.assert_called_with(expected_output)

    def test_take_damage_no_defeat(self):
        player = Player("TestPlayer")
        with patch('sys.stdout', new_callable=MagicMock) as mock_stdout:
            player.take_damage(50)
            expected_output = ""
            mock_stdout.assert_not_called()

    # Add more tests as needed...

class TestGame(unittest.TestCase):
    def test_print_stats(self):
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        player1.total_damage_dealt = 50
        player2.total_damage_dealt = 40
        game = Game(player1, player2)
        with patch('sys.stdout', new_callable=MagicMock) as mock_stdout:
            game.print_stats()
            expected_output = "\n--- Game Stats ---\nPlayer 1 Health: 100\nPlayer 2 Health: 100\nTotal Damage Dealt by Player 1: 50\nTotal Damage Dealt by Player 2: 40."
            mock_stdout.assert_called_with(expected_output)

    # Add more tests as needed...

if __name__ == '__main__':
    unittest.main()
