import unittest
import pig_latin

class TestPigLatin(unittest.TestCase):
    
    def test_find_prefix(self):
        self.assertEqual(pig_latin.find_prefix("bananas"), "b")
        self.assertEqual(pig_latin.find_prefix("sTream"), "str")
        self.assertEqual(pig_latin.find_prefix("Another"), "")
        self.assertEqual(pig_latin.find_prefix("a"), "")

    def test_reverse_stem(self):
        self.assertEqual(pig_latin.reverse_stem("bananas"), "ananasb")
        self.assertEqual(pig_latin.reverse_stem("Stream"), "Eamstr")
        self.assertEqual(pig_latin.reverse_stem("another"), "another")
        self.assertEqual(pig_latin.reverse_stem("a"), "a")

    def test_check_vowels_words(self):
        self.assertEqual(pig_latin.check_vowels_word("bananas"), False)
        self.assertEqual(pig_latin.check_vowels_word("I"), True)
        self.assertEqual(pig_latin.check_vowels_word("iae"), True)

    def test_add_ay(self):
        self.assertEqual(pig_latin.add_ay("bananas"), "bananasay")
        self.assertEqual(pig_latin.add_ay("I"), "Iyay")
        self.assertEqual(pig_latin.add_ay("aie"), "aieyay")

    def test_check_puntuation(self):
        self.assertEqual(pig_latin.pig_latin_word("bananas"), "ananasbay")
        self.assertEqual(pig_latin.pig_latin_word("i"), "iyay")
        self.assertEqual(pig_latin.pig_latin_word("Bananas!"), "Ananasbay!")
       	self.assertEqual(pig_latin.pig_latin_word("buRrito"), "urritobay")

    def test_split_sentence(self):
        self.assertEqual(pig_latin.split_sentence("Hey buddy, get away from my car!"),
        	["Hey", "buddy,","get","away", "from","my","car!"])

    def test_pig_latin_word(self):
        self.assertEqual(pig_latin.pig_latin_word("Bananas!"), "Ananasbay!")

    def test_check_if_real_word(self):
        self.assertEqual(pig_latin.check_if_real_word("bananas"),True)
        self.assertEqual(pig_latin.check_if_real_word("14"),False)
    
    # def main(self):
    #     self.assertEqual(pig_latin.main("Bananas are great!"), "Ananasbay areay eatgray!")

if __name__ == '__main__':
    unittest.main()
