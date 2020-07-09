# Business rule: App
# Entities: Table, Duck


from app.interfaces import TableInterface, DuckInterface
from app.adapters import TableAdapter, DuckAdapter


class App:
    def __init__(self, game_table: TableInterface, game_duck: DuckInterface):
        self.game_table = game_table
        self.game_duck = game_duck

    def run(self):
        """Show initial instructions and start game"""

        print('-------------------------------------------|')
        print('The game was started!                      |')
        print('Be carefull, You can\'t hit in the wall!    |')
        print('After every choice - hit "Enter" :(        |')
        print('-------------------------------------------|')
        print('"W" - up                                   |')
        print('"S" - down                                 |')
        print('"A" - left                                 |')
        print('"D" - right                                |')
        print('                                           |')
        print('       PUSH "ENTER" TO START GAME!         |')
        print('                                           |')
        print('-------------------------------------------|')

        while True:
            press = input()

            self.game_duck.change_position(press)
            self.game_table.show_duck_position(self.game_duck)


if __name__ == '__main__':
    table = TableAdapter(5, 10)
    duck = DuckAdapter()
    app = App(table, duck)
    app.run()
