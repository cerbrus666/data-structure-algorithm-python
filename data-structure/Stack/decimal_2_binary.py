import stack


def divide_by_2(dec_number):
    rem_stack = stack.Stack()

    while dec_number > 0:
        rem = dec_number % 2
        print(rem)
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        print(bin_string)
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


print(divide_by_2(42))
