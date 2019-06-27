# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    print("")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    correctGuess = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            correctGuess = False
    return correctGuess

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    resultString = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            resultString += "_ "
        else:
            resultString = resultString + letter + " "
    return resultString

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in result:
            result = result.replace(letter,'')
    return result

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, lets the user know how many 
      letters the secretWord contains.

    * Asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback after each guess about whether
      their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    '''
    print("Welcome to the game Hangman!")
    print("")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    attempt = 8
    lettersGuessed = []
    while attempt > 0:
        print("")
        print("")
        print("")
        print("--------------------------------------------------")
        print("")
        print("")
        print("")
        print("You have", attempt, "guesses left.")
        print("")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        guess = str(input('Please guess a letter: '))
        print("")
        guessInLowerCase = guess.lower()
        if guessInLowerCase not in lettersGuessed:
            lettersGuessed.extend([guessInLowerCase])
            if guessInLowerCase in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                attempt += -1
            if isWordGuessed(secretWord, lettersGuessed):
                print("")
                print("")
                print("")
                print("--------------------------------------------------")
                print("")
                print("")
                print("")
                print("Congratulations, you won!")
                print("The word was " + secretWord + " as you discovered.")
                return
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
    print("")
    print("")
    print("")
    print("--------------------------------------------------")
    print("")
    print("")
    print("")
    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

keepPlaying = True
playFeedback = 'y'
while keepPlaying:
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    print("")
    print("")
    print("")
    print("--------------------------------------------------")
    print("")
    print("")
    print("")
    playFeedback = str(input('Would you like to play again? (y/n): '))
    print("")
    if ((playFeedback != 'y') and (playFeedback != 'Y') and (playFeedback != 'yes') and (playFeedback != 'Yes')):
        keepPlaying = False