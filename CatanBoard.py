class CatanBoard():
    def __init__(self):
        self.board = nx.random_lobster(10, .5, .2)

    def __str__(self):
        return self.board.nodes().__str__()

    def __repr__(self):
        return self.__str__()

    def randomize_board(self):
        pass

    def create_board(self):
        pass

    def create_board_scaffolding(self):
        pass

    def populate_tiles(self):
        pass

    def populate_dice_nums(self):
        pass

    def populate_ports(self):
        pass
