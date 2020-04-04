"""Module containing all unit that can be spawn in the game"""

import pymunk
import cfg
import math

class Player:
    """Playe class, should be controlled, explicitly"""

    """Player flap direction is has up component"""
    dir_up = False

    """Player flap direction is has down component"""
    dir_down = False

    """Player flap direction is has left component"""
    dir_left = False

    """Player flap direction is has right component"""
    dir_right = False

    def __init__(self, space):
        """Player: add a circle body in the physic space"""
        self.body = pymunk.Body(cfg.PLAYER_MASS, 1000)
        self.body.position = 10, 10
        self.shape = pymunk.Circle(self.body, cfg.PLAYER_RADIUS)
        self.body.velocity_func = self.velocity_func
        space.add(self.body, self.shape)

    def velocity_func(self, body, gravity, damping, dt):
        """velocity_func for player, currently use default pymunk.update_velocity"""
        pymunk.Body.update_velocity(body, gravity, damping, dt)

    def flap(self):
        """Flap wings: add an impulse in a direction, direction must be a tuple with 2 number, does not need to be normalized"""

        # Compute direction to target for the flap
        dir = [self.dir_right - self.dir_left, self.dir_up - self.dir_down]
        # Norm of the direction
        norm = math.sqrt(dir[0]**2 + dir[1]**2)
        # Do not flap if the direction is (0, 0)
        if norm == 0: return
        # Coef to the direction: normalize direction and multiply by PLAYER_FLAP_IMPULSE
        coef = cfg.PLAYER_FLAP_IMPULSE / norm
        self.body.apply_impulse_at_local_point((dir[0]*coef, dir[1]*coef))

class Wall:
    def __init__(self, space):
        """Wall: add a segment body in the physic space"""
        self.body = pymunk.Body(1, 1, pymunk.Body.STATIC)
        self.body.position = 0, 0
        a = 0, 0
        b = 18, 0
        self.shape = pymunk.Segment(self.body, a, b, cfg.WALL_RADIUS)
        space.add(self.body, self.shape)
