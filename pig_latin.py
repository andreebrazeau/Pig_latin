import string

VOWELS = ['a','e','i','o','u','y']
PUNCTUATION = ['.',',','"', "'", ':',';','!','?','(',')']
ALPHABET = string.lowercase + string.uppercase 

def split_sentence(sentence):
    """function that take a sentence and will 
    return a list that contain all the words"""
    sentence = string.split(sentence)
    return sentence


def find_prefix(word):
    """find_prefix if a function that take a word and
    return a substring containing the first letters of the 
    word before it hit a vowel. Will return empty string
    if the word start with a vowel."""
    substring = ""
    for char in word.lower():
        if char in VOWELS:
            return substring
        else:
            substring += char
    return ""

def reverse_stem(word):
    """the function 'reverse_stem' take one argument (str) and 
    will return the reversed word. The reversed word is the
    initial prefix found with the function 'find_prefix' 
    removed frof the word and put at the end"""
    reversed_word = ""
    capitalize = False
    
    #Check if the word is capitalise
    if word[0] == word[0].upper():
        capitalize = True

    word = word.lower()
    prefix = find_prefix(word)
    stem = word.replace(prefix,"")#Remove the prefix of the word
    reversed_word = stem + prefix 

    if capitalize:
        reversed_word = reversed_word.capitalize()

    return reversed_word        

def check_vowels_word(word):
    """The function 'check_vowels_word' take a argument (str)
    and will return 'True' if the word is only compose by vowels
    and will return 'False' other time"""
    for char in word.lower():
        if char not in VOWELS:
            return False
    return True

def check_punctuation(word):
    """The function 'check_punctuation' take one argument 
    (str) and return three strigs. 'begening' and 'end' will
    will be a punctuation if the word included one. 'word' 
    will be the argument 'word' without the punctuations."""
    beginning = ""
    end = ""
    if word[0] in PUNCTUATION:
        beginning += word[0]
        word = word[1:]
    if word[-1] in PUNCTUATION:
        end += word[-1]
        word = word[:-1]
    return (beginning,end,word)

def add_ay(word):
    """The function add_ay thake one argment (str) and return
    the word added with yay if the word if compose by only
    vowels and added ay if not."""
    if check_vowels_word(word):
        return word + "yay"
    else:
        return word + "ay"    

def pig_latin_word(word):
    """The function 'pig_latin_word' take one argument (str)
    and will return the sting reversed, with ay added and with 
    the good puntiation."""
    beginning, end, word = check_punctuation(word)
    if check_if_real_word(word):
        word = add_ay(reverse_stem(word))
    return beginning + word + end

def check_if_real_word(word):
    """The function 'check_if_real_word' take one argument (str)
    and return bolean. Will return False if the word contains
    none alphabet character. Will return True else way."""
    for char in word:
        if char not in ALPHABET:
            return False
            break
    return True

def main():
    while True:
        try:
            print "Type your word. It will be printed to pig latin"
            sentence = raw_input("> ")
        except EOFError:
            #exit if the user enter ^D.
            print "Bye Bye!"
            break
        sentence = split_sentence(sentence)
        final = ""
        for word in sentence:
            new_word = ""
            new_word += pig_latin_word(word)
            final += new_word + " "
        print final

if __name__ == '__main__':
    main()

