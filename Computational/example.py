
def has_in_order(vowels,word):
    # print "Are " + vowels + " in " + word + "?"
    if vowels == "":
        return True
    if word == "":
        return False
    if vowels[0] == word[0]:
        return has_in_order(vowels[1:],word[1:])
    return has_in_order(vowels,word[1:])

def get_words():
    f = open("words.txt")
    words = f.read().split("\n")
    f.close()
    return words #[-20:]


def tests():
    vowels = "aeiou"
    print has_in_order(vowels,"zoo")
    print has_in_order(vowels,"antireligious")

    words = get_words()
    for word in words:
        print word

def count_qualifying_words(vowels, words):
    n = 0
    for word in words:
        if (has_in_order(vowels,word)):
            n = n + 1
            print word
    return n

if __name__ == "__main__":
    words = get_words()
    #vowels = "aeiou"
    vowels = "aeiouy"
    #vowels = "uoiea"
    print count_qualifying_words(vowels, words), "words found out of", len(words), "total words."
