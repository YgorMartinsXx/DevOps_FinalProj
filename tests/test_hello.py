import unittest
from hello import hello

class HelloTest(unittest.TestCase):

    def test_return(self):
        var_hello = hello()
        self.assertEqual(var_hello, ('Hello, DevOps!', 200))


if __name__ == '__main__':
    unittest.main()