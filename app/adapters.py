from app.interfaces import TableInterface, DuckInterface


class DuckAdapter(DuckInterface):
    def __init__(self):
        self.x = 0
        self.y = 0

    def change_position(self, press):
        if press.lower() == 'w':
            self.y -= 1
        if press.lower() == 's':
            self.y += 1
        if press.lower() == 'a':
            self.x -= 1
        if press.lower() == 'd':
            self.x += 1


class TableAdapter(TableInterface):
    def __init__(self, width: int = 6, height: int = 9):
        self.width = width
        self.height = height

    def show_duck_position(self, duck: DuckInterface):
        if duck.x in range(self.width) and duck.y in range(self.height):

            # Init empty table
            result = []
            for y in range(self.height):
                line = ['[ ]' for position in range(self.width)]
                result.append(line)

            # Insert duck into table
            result[duck.y][duck.x] = '[*]'

            # Display duck on table (iter)
            for line in result:
                print(line)

            return True
        else:
            print('Duck hit to the border!')
            print('GAME OVER!')
            return False
