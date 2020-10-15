def validate_nric(input_nric=""):

    # 'TXXXXXXXXXXA'

    if len(input_nric) != 9:
        # NRIC length has to be 9
        return False
    first_char = input_nric[0]
    last_char = input_nric[-1]
    numbers = input_nric[1:-1]

    if first_char.isnumeric():
        return False

    if last_char.isnumeric():
        return False

    if not numbers.isnumeric():
        return False

    mul = [2, 7, 6, 5, 4, 3, 2]

    summation = 0
    for idx, digit in enumerate(numbers):
        summation += int(digit) * mul[idx]

    if first_char.lower() == 't' or first_char.lower() == 'g':
        summation += 4

    remainder = summation % 11
    idx_st = list('JZIHGFEDCBA')
    idx_fg = list('XWUTRQPNMLK')

    if first_char.lower() == 's' or first_char.lower() == 't':
        return last_char.upper() == idx_st[remainder]

    if first_char.lower() == 'f' or first_char.lower() == 'g':
        return last_char.upper() == idx_fg[remainder]

    return False
