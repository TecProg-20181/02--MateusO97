import random
import string
from sets import Set

WORDLIST_FILENAME = "palavras.txt"

def lettersNumber(word, guesses):
    differentLetters = Set(list(word))
    lettersQuantity = len(differentLetters)
    if lettersQuantity > guesses:
        loadWords()
    print "The word has: ", lettersQuantity, "different letters."

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True

def getGuessedWord():
     guessed = ''
     return guessed

def getAvailableLetters(lettersGuessed):
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    print 'Available letters', available

def triedLetter(letter, lettersGuessed):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Oops! You have already guessed that letter: ', guessed

def correctLetter(letter, lettersGuessed, secretWord):
    lettersGuessed.append(letter)
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Good Guess: ', guessed

def wrongLetter(letter, lettersGuessed, secretWord):
    lettersGuessed.append(letter)
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print 'Oops! That letter is not in my word: ',  guessed

def inputLetter(guesses, lettersGuessed, secretWord):
    print 'You have ', guesses, 'guesses left.'
    getAvailableLetters(lettersGuessed)
    letter = raw_input('Please guess a letter: ')
    if letter in lettersGuessed:
        triedLetter(letter, lettersGuessed)
    elif letter in secretWord:
        correctLetter(letter, lettersGuessed, secretWord)
    else:
        guesses -=1
        wrongLetter(letter, lettersGuessed, secretWord)
    print '------------'
    return guesses

def menu(secretWord):
            print 'Welcome to the game, Hangam!'
            print 'I am thinking of a word that is', len(secretWord), ' letters long.'
            print '-------------'

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    menu(secretWord)
    lettersQuantity = lettersNumber(secretWord, guesses)
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
            guesses = inputLetter(guesses, lettersGuessed, secretWord)
    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

secretWord = loadWords().lower()
hangman(secretWord)
