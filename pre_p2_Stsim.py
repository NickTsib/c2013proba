import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.prog = 0
        self.alive = True

    def to_stud(self):
        print("Time to study")
        self.prog += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.prog -= 0.1

    def is_alive(self):
        if self.prog < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.prog > 5:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.prog, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_stud()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
lisa = Student(name="Lisa")

for day in range(365):
    if nick.alive:
        nick.live(day)
    if lisa.alive:
        lisa.live(day)
    if not nick.alive and not lisa.alive:
        break
