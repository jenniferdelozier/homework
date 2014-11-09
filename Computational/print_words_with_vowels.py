
def has_in_order(vowels,word):
    # print "Are " + vowels + " in " + word + "?"
    # this looks for a match for the first vowel, 
	# if the first vowel is found, it looks for the remaining vowels in the rest of the word 
	# if the first vowel is not found, it looks for all of the vowels in the rest of the word
    if vowels == "":
        return True
    if word == "":
        return False
    if vowels[0] == word[0]:
        return has_in_order(vowels[1:],word[1:])
    return has_in_order(vowels,word[1:])

#this gets all of the text and splits it into single words. It also gets rid of unwanted characters.  
def get_words():
    f = open("words.eggs")
    words = f.read().replace("\r","").split("\n")
    f.close()
    return words 

#This was a test to make sure that the program was functioning
def tests():
    vowels = "aeiou"
    print has_in_order(vowels,"zoo")
    print has_in_order(vowels,"antireligious")

    words = get_words()
    for word in words:
        print word
#This prints the qualifying words
def print_qualifying_words(vowels, words):
    for word in words:
        if (has_in_order(vowels,word)):
            print word

if __name__ == "__main__":
    words = get_words()
    vowels = "aeiou"
    print_qualifying_words(vowels, words)
