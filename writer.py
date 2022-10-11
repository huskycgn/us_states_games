from turtle import Turtle


class Write(Turtle):
    def __init__(self):
        super().__init__()

    def writeState(self, statename, xc, yc):
        xwrite = xc
        ywrite = yc
        self.setposition(x=xwrite, y=ywrite)
        self.write(statename)
