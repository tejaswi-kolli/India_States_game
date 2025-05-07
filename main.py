import turtle
import pandas
screen = turtle.Screen()
screen.title("India States Game")
image = "India_States.gif"
screen.addshape(image)
turtle.shape(image)
# to find the x,y values by clicking on the state
# def get_mouse_click_coor(x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data=pandas.read_csv("29_states_of_India.csv")
states_list=data["State"].to_list()
guessed_states=[]
while len(guessed_states)<29:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/29 States Correct",prompt="What's another State Name?").title()
    if answer_state=="Exit":
        missed_states=[]
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["State"]==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.State.item())
