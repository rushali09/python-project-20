from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

hello_kitty = True

while hello_kitty:
    screen.update()
    time.sleep(0.5)
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.grow()
        score.increase_score()

    # Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() < -280:
        hello_kitty = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            hello_kitty = False
            score.game_over()














screen.exitonclick()















