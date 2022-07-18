import random


class Hat:

    def __init__(self, **kwargs):
        self.contents_init = []
        for k, v in kwargs.items():
            for n in range(v):
                self.contents_init.append(k)

    def draw(self, number):

        self.contents = self.contents_init.copy()
        if number >= len(self.contents):
            return self.contents
        else:
            chosen_list = []
            for n in range(number):
                chosen_ball = random.choice(self.contents)
                chosen_list.append(chosen_ball)
                self.contents.remove(chosen_ball)
        return chosen_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success_num = 0
    for n in range(num_experiments):

        draw_list = hat.draw(num_balls_drawn)
        condition_list = []
        for k, v in expected_balls.items():
            if k in draw_list:
                if v <= draw_list.count(k):
                    condition_list.append(True)

                else:
                    condition_list.append(False)
            else:
                condition_list.append(False)

        if False not in condition_list:
            success_num += 1

    return success_num / num_experiments

