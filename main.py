countdown = 5
counter = countdown
for index in range(countdown + 1):
    basic.show_number(counter)
    counter += -1

def on_forever():
    pass
basic.forever(on_forever)
