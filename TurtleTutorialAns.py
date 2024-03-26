# Import turtle library
import turtle

# Create turtle screen
screen = turtle.Screen()

# Create a turtle 
drawing_turtle = turtle.Turtle()

# Create variables for turtle
turtle_speed = 5
turtle_turn_degree = 90
turtle_move_distance = 100

# Set the speed of the turtle
drawing_turtle.speed(turtle_speed)  # Speeds range from 1 (slowest) to 10 (fastest). 0 means no animation.

# Drawing a square
drawing_turtle.forward(turtle_move_distance)  # Move the turtle forward by 100 units
drawing_turtle.right(turtle_turn_degree)     # Rotate the turtle by 90 degrees to the right

drawing_turtle.forward(turtle_move_distance)  # Move the turtle forward by 100 units
drawing_turtle.right(turtle_turn_degree)     # Rotate the turtle by 90 degrees to the right

drawing_turtle.forward(turtle_move_distance)  # Move the turtle forward by 100 units
drawing_turtle.right(turtle_turn_degree)     # Rotate the turtle by 90 degrees to the right

drawing_turtle.forward(turtle_move_distance)  # Move the turtle forward by 100 units
drawing_turtle.right(turtle_turn_degree)     # Rotate the turtle by 90 degrees to the right

# To keep the window open until it is closed manually
turtle.done()
