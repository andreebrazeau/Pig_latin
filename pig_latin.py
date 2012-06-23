import string

vowels = ['a','e','i','o','u','y']
punctuation = ['.',',','"', "'", ':',';','!','?','(',')']
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def split_sentence(sentence):
	sentence = string.split(sentence)
	return sentence


def find_prefix(word):
	substring = ""
	for char in word.lower():
		if char in vowels:
			return substring
		else:
			substring += char
	return ""

def reverse_stem(word):
	reversed_word = ""
	capitalize = False
	if word[0] == word[0].upper():
		capitalize = True
	word = word.lower()
	prefix = find_prefix(word)
	stem = word.replace(prefix,"") 
	reversed_word = stem + prefix 
	if capitalize:
		reversed_word = reversed_word.capitalize()
	return reversed_word		

def check_vowels_word(word):
	for char in word.lower():
		if char not in vowels:
			return False
	return True

def check_punctuation(word):
	beginning = ""
	end = ""
	if word[0] in punctuation:
		beginning += word[0]
		word = word[1:]
	if word[-1] in punctuation:
		end += word[-1]
		word = word[:-1]
	return (beginning,end,word)

def add_ay(word):
	if check_vowels_word(word):
		return word + "yay"
	else:
		return word + "ay"	

def pig_latin_word(word):
	beginning, end, word = check_punctuation(word)
	word = add_ay(reverse_stem(word))
	return beginning + word + end


def main():
	while True:
		try:
			print "Type your word. It will be printed to pig latin"
			sentence = raw_input("> ")
		except EOFError:
			print "Bye Bye!"
			break
		sentence = split_sentence(sentence)
		final = ""
		for word in sentence:
			new_word = ""
			for char in word:
				if char not in alphabet:
					new_word += word
					break
			
			new_word += pig_latin_word(word)
				
			final += new_word + " "
		print final
		return final

if __name__ == '__main__':
	main()

