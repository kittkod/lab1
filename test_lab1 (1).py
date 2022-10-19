import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        self.assertEqual(q.dequeue(), None)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
    def test_dequeue(self):
        # testing basic dequeue operation
        q = lab1.Queue()
        self.assertEqual(q.dequeue(), RuntimeError("Dequeuing from an empty Queue."))
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.__str__(), '[3, 4]')
    def test_isEmpty(self):
        # testing isEmpty operation
        q = lab1.Queue()
        q.enqueue(7)
        self.assertEqual(q.isEmpty(), False) 
        q.dequeue()
        self.assertEqual(q.isEmpty(), True)    
    def test_letters_and_spaces(self):
        # testing if letters and spaces work as input
        q = lab1.Queue()
        q.enqueue('H')
        q.enqueue(' ')
        self.assertEqual(q.__str__(), "['H', ' ']")

        print("\n")

class T1_TestingStack(unittest.TestCase):

    def test_is_empty(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        s.pop()
        self.assertEqual(s.isEmpty(), True)
    def test_push(self):
        # testing is push works correctly
        s = lab1.Stack()
        s.push(4)
        s.push(54)
        s.push(9)
        self.assertEqual(s.__str__(), '[9, 54, 4]')
    def test_pop(self):
        s = lab1.Stack()
        s.push(1)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.__str__(), '[]')
        self.assertEqual(s.pop(), RuntimeError("Popping from an empty stack."))
    def test_letters_and_spaces(self):
        # testing if letters and spaces work as input
        s = lab1.Stack()
        s.push('H')
        s.push(' ')
        self.assertEqual(s.__str__(), "[' ', 'H']")
        
        print("\n")

class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "Hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
    def test_upper_and_space(self):
        # testing a palindrome with upper and lowercase
        string = "TaCo CaT"
        p = lab1.isPalindrome(string)
        self.assertEqual(p, True)
        
        print("\n")

if __name__ == '__main__':
    unittest.main()
