from codejam import jam


def standing_ovation(audience):
    standing = 0
    additions = 0
    for shy_level, amount in enumerate(audience):
        amount = int(amount)
        if standing >= shy_level:
            standing += amount
        elif amount != 0:
            addition = shy_level - standing
            standing += addition + amount
            additions += addition
    return additions


jam("A-large.in", standing_ovation)