#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

rex = Dog("Rex", "Poodle")
print(rex.breed)

jelly = Dog("Jelly")
print(jelly.breed)
