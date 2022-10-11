import turtle
import pandas
from writer import Write

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(width=800, height=500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(False)
turtle.penup()


states = pandas.read_csv('50_states.csv')
writer = Write()
statelist = states['state']
x_cor = states['x']
y_cor = states['y']

state_dict = {}
score = 0

for index, s in enumerate(statelist):
    state_dict[s] = x_cor[index], y_cor[index]

correct_states = []

# print(state_dict['Texas'])

while score < len(statelist):

    answer_state = screen.textinput(title=f'Guess the State Score: {score}', prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == 'Exit':
        break
    if answer_state in state_dict:
        xwrite = state_dict[answer_state][0]
        ywrite = state_dict[answer_state][1]
        writer.writeState(answer_state, xwrite, ywrite)
        state_dict.pop(answer_state)
        score += 1
        correct_states.append(answer_state)

states_to_learn = []
for s in state_dict:
    states_to_learn.append(s)


states_to_learn = pandas.DataFrame(states_to_learn)
states_to_learn.to_csv('states_to_learn.csv')