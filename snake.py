# This file creates the snake and sets its capabilites 
STARTING_POSITIONS= [(-20,0), (0,0), (20,0)]
MOVE_DISTANCE= 20
DOWN= 270
UP = 90
LEFT = 180
RIGHT = 0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
#   This step creates the snake    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
#   The following some lines determine the snakes movements by setting the heading to different angles    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
#   This step extends the snake when eating food, which is set in the main.py file   
    def extend(self):
        self.add_segment(self.segments[-1].position())
#   This step allows for the snake to be reset once running into the walls or itself, which is set in the main.py file   
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
