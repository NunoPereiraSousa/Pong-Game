window_width = 1024
window_height = 700

class Ball():
    def __init__(self):
        self.x = int(window_width / 2)
        self.y = int(window_height / 2)
        self.radius = 10
        self.vx = 5
        self.vy = 5
        self.dt = 1
        self.vel = 5