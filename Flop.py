from FlopTags import FlopTags

card_rankings = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

class Card:
    def __init__(self, card_name, suit):
        self.card_name = card_name
        self.rank = card_rankings[card_name]
        self.suit = suit

class Flop:
    def __init__(self, c1, c2, c3):
        self.cards = sorted([Card(c1[0], c1[1]), Card(c2[0], c2[1]), Card(c3[0], c3[1])], key=lambda x: x.rank, reverse=True)
        self.high_card_tag = self._getHighCardTag()


    def _getHighCardTag(self):
        highCard = self.cards[0]  
        if highCard.card_name == "A":
            return FlopTags._A_HIGH
        elif highCard.card_name == "K":
            return FlopTags._K_HIGH
        elif highCard.card_name == "Q":
            return FlopTags._Q_HIGH
        elif highCard.card_name == "J":
            return FlopTags._J_HIGH
        elif highCard.card_name == "T":
            return FlopTags._T_HIGH
        elif highCard.card_name == "9":
            return FlopTags._9_HIGH
        elif highCard.card_name == "8":
            return FlopTags._8_HIGH
        elif highCard.card_name == "7":
            return FlopTags._7_HIGH
        elif highCard.card_name == "6":
            return FlopTags._6_HIGH
        elif highCard.card_name == "5":
            return FlopTags._5_HIGH
        elif highCard.card_name == "4":
            return FlopTags._4_HIGH
        elif highCard.card_name == "3":
            return FlopTags._3_HIGH
        elif highCard.card_name == "2":
            return FlopTags._2_HIGH
        
    # def _getPairInfo(self):
        