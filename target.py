from turtle import Turtle, TurtleGraphicsError


class Target(Turtle):

    def __init__(self, target_number=1, start_x=0, start_y=0, img_width=50, img_height=50, lenght=15):
        super().__init__()
        self.color("white")
        self.reset()
        self.penup()
        self.target_number = target_number
        self.start_x = start_x
        self.start_y = start_y
        self.width = img_width
        self.height = img_height
        self.lenght = lenght
        self.first_x_start = start_x
        self.target_objects = []

    def my_shape(self, path=None):
        for index in range(self.target_number):
            target = Target()
            try:
                target.shape(path)
                self.width = target.width
                self.height = target.height
            except TurtleGraphicsError:
                target.shape("circle")
                self.width = target.width
                self.height = target.height
            self.target_objects.append(target)

    def display(self):
        for index in range(len(self.target_objects)):
            if not index:
                self.start_x = self.start_x
            elif index % self.lenght == 0:
                self.start_y -= self.height + 2
                self.start_x = self.first_x_start
            else:
                self.start_x += self.width
            self.target_objects[index].goto(self.start_x, self.start_y)
        return self.target_objects
