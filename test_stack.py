import unittest
from stack import LessThenTwoElement
from stack import RegisterAlreadyEmpty
from stack import UnknownFifthCommand
from stack import FifthStack
from stack import FifthInterpreter


class MyTestCase(unittest.TestCase):
    def test_push(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 6")
        fifth_interpreter.process_input("PUSH 5")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [11, 6, 5]")

    def test_pop(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("POP")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is []")

    def test_dup(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 2")
        fifth_interpreter.process_input("DUP")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [22, 4]")

    def test_swap(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 5")
        fifth_interpreter.process_input("PUSH 6")
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 2")
        fifth_interpreter.process_input("SWAP")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [5, 6, 2, 11]")

    def test_add(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 5")
        fifth_interpreter.process_input("PUSH 6")
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 2")
        fifth_interpreter.process_input("+")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [5, 6, 13]")

    def test_substract(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 5")
        fifth_interpreter.process_input("PUSH 6")
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 4")
        fifth_interpreter.process_input("-")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [5, 6, 7]")

    def test_multiply(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 5")
        fifth_interpreter.process_input("PUSH 6")
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 7")
        fifth_interpreter.process_input("*")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [5, 6, 77]")

    def test_divide(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 5")
        fifth_interpreter.process_input("PUSH 6")
        fifth_interpreter.process_input("PUSH 11")
        fifth_interpreter.process_input("PUSH 7")
        fifth_interpreter.process_input("/")
        self.assertEqual(fifth_interpreter.stack_state(), "stack is [5, 6, 1]")

    def test_register_already_empty(self):
        fifth_interpreter = FifthInterpreter()
        with self.assertRaises(RegisterAlreadyEmpty):
            fifth_interpreter.process_input("POP")

    def test_less_then_two_element_for_swap(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 3")
        with self.assertRaises(LessThenTwoElement):
            fifth_interpreter.process_input("SWAP")

    def test_less_then_two_element_for_dup(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 3")
        with self.assertRaises(LessThenTwoElement):
            fifth_interpreter.process_input("DUP")

    def test_less_then_two_element_for_add(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 3")
        with self.assertRaises(LessThenTwoElement):
            fifth_interpreter.process_input("+")

    def test_less_then_two_element_for_substract(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 3")
        with self.assertRaises(LessThenTwoElement):
            fifth_interpreter.process_input("-")

    def test_less_then_two_element_for_multiply(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 3")
        with self.assertRaises(LessThenTwoElement):
            fifth_interpreter.process_input("*")

    def test_less_then_two_element_for_divide(self):
        fifth_interpreter = FifthInterpreter()
        fifth_interpreter.process_input("PUSH 3")
        with self.assertRaises(LessThenTwoElement):
            fifth_interpreter.process_input("/")


    def test_less_unknown_fifth_command(self):
        fifth_interpreter = FifthInterpreter()
        with self.assertRaises(UnknownFifthCommand):
            fifth_interpreter.process_input("PUHS 3")

if __name__ == '__main__':
    unittest.main()
