import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents = []
            return drawn

        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        drawn_counts = {}
        for ball in drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        match = all(
            drawn_counts.get(color, 0) >= count
            for color, count in expected_balls.items()
        )
        if match:
            success += 1

    return success / num_experiments
