import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    
    with open("/home/rhutujapatil/Desktop/Hangman/e-sreedharan-master/hangman/words.txt", 'r')as inFile:
        line = inFile.read()

        word_list = line.split()

        # a=word_file.read()
        # word_list=a.split()
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word