
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
    words = f.read().split("\n")
    f.close()
    return words #[-20:]

#This was a test to make sure that the program was functioning
def tests():
    vowels = "aeiou"
    print has_in_order(vowels,"zoo")
    print has_in_order(vowels,"antireligious")

    words = get_words()
    for word in words:
        print word

#this counts the qualifying words
def count_qualifying_words(vowels, words):
    n = 0
    for word in words:
        if (has_in_order(vowels,word)):
            n = n + 1
    return n

if __name__ == "__main__":
    words = get_words()
    vowels = "aeiou"
    print count_qualifying_words(vowels, words), "words found out of", len(words), "total words."
