import sys

class FifthStack(object):
    def __init__(self):
        self.__register = []

    def push(self, x: int):
        self.__register.append(x)

    def pop(self):
        length = len(self.__register)
        if length == 0:
            raise RegisterAlreadyEmpty("Not possible to pop")
        else:
            self.__register.pop(length - 1)

    def swap(self):
        length = len(self.__register)
        if length >= 2:
            last_but_one_element = self.__register[length - 2]
            self.__register.pop(length - 2)
            self.push(last_but_one_element)
        else:
            raise LessThenTwoElement("Not possible to swap")

    def dup(self):
        length = len(self.__register)
        if length >= 2:
            self.__register[length - 1] = (self.__register[length - 1]) * 2
            self.__register[length - 2] = (self.__register[length - 2]) * 2
        else:
            raise LessThenTwoElement("Not possible to duplicate")

    def add(self):
        length = len(self.__register)
        if length >= 2:
            self.__register[length - 2] = (self.__register[length - 2]) + (self.__register[length - 1])
            self.pop()
        else:
            raise LessThenTwoElement("Not possible to add")

    def substract(self):
        length = len(self.__register)
        if length >= 2:
            self.__register[length - 2] = (self.__register[length - 2]) - (self.__register[length - 1])
            self.pop()
        else:
            raise LessThenTwoElement("Not possible to substract")

    def multiply(self):
        length = len(self.__register)
        if length >= 2:
            self.__register[length - 2] = (self.__register[length - 2]) * (self.__register[length - 1])
            self.pop()
        else:
            raise LessThenTwoElement("Not possible to multiply")

    def divide(self):
        length = len(self.__register)
        if length >= 2:
            self.__register[length - 2] = (self.__register[length - 2]) // (self.__register[length - 1])
            self.pop()
        else:
            raise LessThenTwoElement("Not possible to divide")

    def to_string(self):
        return "stack is " + str(self.__register)


class FifthInterpreter(object):
    def __init__(self):
        self.__fifth_stack = FifthStack()

    def process_input(self, interpreter_input: str):
        interpreter_input = interpreter_input.lstrip()
        if interpreter_input.startswith("PUSH"):
            x = int(interpreter_input[4:])
            self.__fifth_stack.push(x)
        elif interpreter_input.startswith("POP"):
            self.__fifth_stack.pop()
        elif interpreter_input.startswith("SWAP"):
            self.__fifth_stack.swap()
        elif interpreter_input.startswith("DUP"):
            self.__fifth_stack.dup()
        elif interpreter_input.startswith("+"):
            self.__fifth_stack.add()
        elif interpreter_input.startswith("-"):
            self.__fifth_stack.substract()
        elif interpreter_input.startswith("*"):
            self.__fifth_stack.multiply()
        elif interpreter_input.startswith("/"):
            self.__fifth_stack.divide()
        else:
            raise UnknownFifthCommand("Can not execute command")

    def stack_state(self):
        return self.__fifth_stack.to_string()


class UnknownFifthCommand(Exception):
    pass


class LessThenTwoElement(Exception):
    pass


class RegisterAlreadyEmpty(Exception):
    pass


def main():
    if (sys.version_info < (3, 0)):
        print("This tool needs python3! ")
        sys.exit(1)
    print("Please type Fifth supported commands:")
    fifth_interpreter = FifthInterpreter()
    while True:
        try:
            fifth_interpreter.process_input(input(""))
            print(fifth_interpreter.stack_state())
        except Exception as e:
            print(repr(e))


if __name__ == "__main__":
    main()
