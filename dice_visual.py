from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
results =[die1.roll()+die2.roll() for i in range(1000)]

frequencies = []
frequencies = [results.count(value) for value in range(2, die1.num_sides*2+1 )]



hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(2, die1.num_sides*2+1))
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')





