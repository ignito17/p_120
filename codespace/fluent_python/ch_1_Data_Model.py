# Example 1-1. A deck as a sequence of playing cards 
import collections 
Card = collections.namedtuple('Card', ['rank', 'suit']) 
class FrenchDeck: 
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
    suits = 'spades diamonds clubs hearts'.split() 
    def __init__(self): 
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] 
    def __len__(self): 
        return len(self._cards) 
    def __getitem__(self, position): 
        return self._cards[position]
    
# beer_card=Card('7', 'diamonds')
# print(beer_card)
deck_1 = FrenchDeck()
deck_2 = FrenchDeck()

from random import choice

# print(choice(deck_1),choice(deck_2))
# print(deck_1[:5], deck_2[-1:-2:-1])  # Slicing works as expected
