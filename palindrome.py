import unittest;

def test(word):
    test = "";
    for letter in word:
        test = letter + test;
    if word == test:
        return True;
    else:
        return False;

class palindromeTest(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(test("neuquen"), True);
    def test_dos(self):
        self.assertEqual(test("ana"), True);
    def test_tres(self):
        self.assertEqual(test("lisandro"), False)
if __name__ == '__main__':
    unittest.main();    