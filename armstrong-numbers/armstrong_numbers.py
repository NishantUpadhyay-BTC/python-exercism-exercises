def is_armstrong_number(number):
    digits = list(map(int, str(number)))
    total_count = len(digits)
    power_arr = [digit ** total_count for digit in digits]
    return sum(power_arr) == number
