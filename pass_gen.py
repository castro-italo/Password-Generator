import random


from const import NUMBERS, CHAR



class GenPass(object):
    def __init__(self) -> None:
        self.numbers = len(NUMBERS)
        self.char = len(CHAR)

    # Generate password just with numbers
    def just_num(self):
        result = list()
        passw = str()
        for _ in range(10):
            idx = random.randint(0, self.numbers - 1)
            result.append(str(NUMBERS[idx]))
        passw = ' '.join(result)

        return passw

    def just_char(self):
        result = list()
        passw = str()
        for _ in range(10):
            idx = random.randint(0, self.char - 1)
            result.append(CHAR[idx])
        passw = ' '.join(result)

        return passw

    def number_char(self):
        result = list()
        passw = ""
        for i in range(10):
            if(i % 2 == 0):
                idx_char = random.randint(0, self.char - 1)
                result.append(CHAR[idx_char])
            else:
                idx_num = random.randint(0, self.numbers - 1)
                result.append(str(NUMBERS[idx_num]))
        passw = ' '.join(result)

        return passw

    def __repr__(self):
        return f"LEN NUMBERS: {self.numbers} | LEN CHAR: {self.char}"
