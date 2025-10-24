import unittest
from io import StringIO
import sys
from src.hello import main

class TestHello(unittest.TestCase):
    def test_main_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
