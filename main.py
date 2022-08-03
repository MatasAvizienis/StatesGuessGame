import turtle 
import os
import pandas as pd
os.chdir(r"C:\Users\matas\Desktop\lol\d25\us-states-game-start")

data = pd.read_csv("50_states.csv")
states_list = data['state'].to_list()

# creating writer
t = turtle.Turtle()
t.penup()
t.hideturtle()

# creating screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# creating loop
guessed_states = []
while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ", prompt="What's another state name?").title()
    if answer_state in states_list and len(guessed_states) != 50:
        guessed_states.append(answer_state)
        states_list.remove(answer_state)
        state_line = data[data.state == f"{answer_state}"]
        t.goto(int(state_line.x), int(state_line.y))
        t.write(answer_state, False, 'center', ('Arial', 8, 'normal'))

    # exit and csv file with missed states in
    if answer_state == 'Exit':
        # 
        first = set(states_list)
        second = set(guessed_states)
        unknown = list(first.difference(second))

        states_to_learn = pd.DataFrame(unknown)
        states_to_learn.to_csv(r"C:\Users\matas\Desktop\lol\d25\us-states-game-start\states_to_learn.csv")
        break

screen.mainloop()