class Utils:
    def reversed(number):
        if isinstance(number, int):
            return int(str(number)[::-1])
        else:
            raise ValueError("Number must be an integer!")

    def formatter(number):
        if isinstance(number, int):
            binary = bin(number)
            octal = oct(number)
            return binary, octal
        else:
            raise ValueError("Number must be an integer!")
