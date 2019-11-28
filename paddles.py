window_width = 1024
window_height = 700

class Paddle1():
    def __init__(self):
        self.x = 20
        self.y = window_height / 2 - 50
        self.width = 15
        self.height = 100
        self.dt = 1

class Paddle2():
    def __init__(self):
        self.x = window_width - 35
        self.y = window_height / 2 - 50
        self.width = 15
        self.height = 100
        self.dt = 1

class PaddleCenter():
    def __init__(self):
        self.x = window_width/2-40/2 
        self.y = 0 
        self.width = 40
        self.height = 200
        self.dt = 1
        self.step = 10