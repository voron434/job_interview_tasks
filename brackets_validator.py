def bracket_validator(input_string):
    opened_brackets_counter = 0
    is_valid = False
    for bracket in input_string:
        if bracket == "(":
            opened_brackets_counter += 1
        elif bracket == ")" and opened_brackets_counter <= 0:
            break
        else:
            opened_brackets_counter -= 1
    else:
        is_valid = opened_brackets_counter == 0
    return is_valid