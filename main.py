# Reaction when Button A is pressed///
def on_button_pressed_a():
    global Name
    Name = randint(1, 17)
    if Name == 1:
        basic.show_string("RAMEN")
    elif Name == 2:
        basic.show_string("BURGER")
    elif Name == 3:
        basic.show_string("BREAD")
    elif Name == 4:
        basic.show_string("TACOS")
    elif Name == 5:
        basic.show_string("BURRITOS")
    elif Name == 6:
        basic.show_string("PASTA")
    elif Name == 7:
        basic.show_string("FRIED-RICE")
    elif Name == 8:
        basic.show_string("WAFFLES")
    elif Name == 9:
        basic.show_string("STEAK")
    elif Name == 10:
        basic.show_string("CUP-NOODLES")
    elif Name == 11:
        basic.show_string("SALAD")
    elif Name == 12:
        basic.show_string("HOT-DOGS")
    elif Name == 13:
        basic.show_string("CHICKEN-WINGS")
    elif Name == 14:
        basic.show_string("ICE-CREAM")
    elif Name == 15:
        basic.show_string("APPLE-PIE")
    elif Name == 16:
        basic.show_string("PIZZA")
    elif Name == 17:
        basic.show_string("CURRY")
input.on_button_pressed(Button.A, on_button_pressed_a)

Name = 0

# Reaction when Button A+B is pressed at the same time///
def on_button_pressed_ab():
    global Name
    Name = randint(1, 17)
    if Name == 1:
        basic.show_string("RAMEN")
    elif Name == 2:
        basic.show_string("BURGER")
    elif Name == 3:
        basic.show_string("BREAD")
    elif Name == 4:
        basic.show_string("TACOS")
    elif Name == 5:
        basic.show_string("BURRITOS")
    elif Name == 6:
        basic.show_string("PASTA")
    elif Name == 7:
        basic.show_string("FRIED-RICE")
    elif Name == 8:
        basic.show_string("WAFFLES")
    elif Name == 9:
        basic.show_string("STEAK")
    elif Name == 10:
        basic.show_string("CUP-NOODLES")
    elif Name == 11:
        basic.show_string("SALAD")
    elif Name == 12:
        basic.show_string("HOT-DOGS")
    elif Name == 13:
        basic.show_string("CHICKEN-WINGS")
    elif Name == 14:
        basic.show_string("ICE-CREAM")
    elif Name == 15:
        basic.show_string("APPLE-PIE")
    elif Name == 16:
        basic.show_string("PIZZA")
    elif Name == 17:
        basic.show_string("CURRY")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Name = 0

# Reaction when Button B is pressed///
def on_button_pressed_b():
    global Name
    Name = randint(1, 17)
    if Name == 1:
        basic.show_string("RAMEN")
    elif Name == 2:
        basic.show_string("BURGER")
    elif Name == 3:
        basic.show_string("BREAD")
    elif Name == 4:
        basic.show_string("TACOS")
    elif Name == 5:
        basic.show_string("BURRITOS")
    elif Name == 6:
        basic.show_string("PASTA")
    elif Name == 7:
        basic.show_string("FRIED-RICE")
    elif Name == 8:
        basic.show_string("WAFFLES")
    elif Name == 9:
        basic.show_string("STEAK")
    elif Name == 10:
        basic.show_string("CUP-NOODLES")
    elif Name == 11:
        basic.show_string("SALAD")
    elif Name == 12:
        basic.show_string("HOT-DOGS")
    elif Name == 13:
        basic.show_string("CHICKEN-WINGS")
    elif Name == 14:
        basic.show_string("ICE-CREAM")
    elif Name == 15:
        basic.show_string("APPLE-PIE")
    elif Name == 16:
        basic.show_string("PIZZA")
    elif Name == 17:
        basic.show_string("CURRY")
input.on_button_pressed(Button.B, on_button_pressed_b)

Name = 0

# Reaction when WHOLE THING shaken///
def on_gesture_shake():
    global Name
    Name = randint(1, 17)
    if Name == 1:
        basic.show_string("RAMEN")
    elif Name == 2:
        basic.show_string("BURGER")
    elif Name == 3:
        basic.show_string("BREAD")
    elif Name == 4:
        basic.show_string("TACOS")
    elif Name == 5:
        basic.show_string("BURRITOS")
    elif Name == 6:
        basic.show_string("PASTA")
    elif Name == 7:
        basic.show_string("FRIED-RICE")
    elif Name == 8:
        basic.show_string("WAFFLES")
    elif Name == 9:
        basic.show_string("STEAK")
    elif Name == 10:
        basic.show_string("CUP-NOODLES")
    elif Name == 11:
        basic.show_string("SALAD")
    elif Name == 12:
        basic.show_string("HOT-DOGS")
    elif Name == 13:
        basic.show_string("CHICKEN-WINGS")
    elif Name == 14:
        basic.show_string("ICE-CREAM")
    elif Name == 15:
        basic.show_string("APPLE-PIE")
    elif Name == 16:
        basic.show_string("PIZZA")
    elif Name == 17:
        basic.show_string("CURRY")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Name = 0

# Music played after startup
music.play_melody("C D E G - - - - ", 400)
basic.show_string("MAGIC-FOOD-BIT")
