def response(hey_bob):
    answer = hey_bob.strip()

    if answer.endswith('?') and answer.isupper():
        return "Calm down, I know what I'm doing!"
    elif answer.endswith('?'):
        return 'Sure.'
    elif answer.isupper():
        return 'Whoa, chill out!'
    elif not answer:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'