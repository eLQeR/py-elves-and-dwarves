from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str
    ) -> None:
        self.favourite_dish = favourite_dish
        super().__init__(nickname)

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")
