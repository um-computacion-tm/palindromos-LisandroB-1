import unittest;

def test(word):
    return word == word[::-1]
    
class recursiveTest(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(test("ana"), True)
    def test_dos(self):
        self.assertEqual(test("asdads"), False)

if __name__ == '__main__':
    unittest.main();  