from Boardgamebox.Player import Player as BasePlayer

class Player(BasePlayer):
    def __init__(self, name, uid):
        BasePlayer.__init__(self, name, uid)
        self.role = "" # Ej: Drunk
        self.afiliation = "" # Good or Evil
        self.townfolk_Outsider_Minion_Demon # Indica cual de los subgrupos es el jugador
        self.poisoned = False # Indica si el jugador esta envenenado
        self.drunk = False # Indica si el jugador esta borracho
        self.nominated_someone = False # Indica si nominaste a alguien esta ronda
        self.was_nominated = False # Indica si fue animado
        self.has_voted = False # Indica si has votado

    def get_private_info(self, game):
        board = "--- Info del Jugador {} en la partida *{}*---\n".format(self.name, game.groupName) 
        return board