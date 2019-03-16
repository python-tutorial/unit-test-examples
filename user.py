import random


class User:
    def add_two_numbers(self, first, second):
        return first+second+self.return_random()

    def return_random(self):
        return random.random()