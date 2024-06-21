import urwid


def has_digit(password):
    return any(i.isdigit() for i in password)


def is_very_long(password):
    return len(password) > 12
 

def has_letters(password):
    return any(i.isalpha() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isalpha() and not i.isdigit() for i in password)


def score_password(password):
    funcs_list = [
        has_digit, 
        is_very_long, 
        has_letters, 
        has_upper_letters, 
        has_lower_letters, 
        has_symbols
    ]
    score = 0
    for func in funcs_list:
        if func(password):
            score +=2
    return score


def on_ask_change(edit, new_edit_text):
    reply.set_text("Вы тайно написали: {text}, Рейтинг пароля: {score}".format(text = new_edit_text, score = score_password(new_edit_text)))


if __name__ == "__main__":
    ask = urwid.Edit('Тайный ввод: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
