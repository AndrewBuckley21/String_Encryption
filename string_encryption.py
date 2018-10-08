# LAB4.py


def answers():
    question_a = "126"
    question_b = "0,2,4,6,8"
    question_c = "0"

    return question_a, question_b, question_c


def encrypt(message, key):
    lowerAlphabet ="abcdefghijklmnopqrstuvwxyz"
    newLowerAlphabet = lowerAlphabet[key:] + lowerAlphabet[:key]
    upperAlphabet = lowerAlphabet.upper()
    newUpperAlphabet = newLowerAlphabet.upper()

    encMessage=""
    for character in message:
        if character in lowerAlphabet:
            encMessage += newLowerAlphabet[lowerAlphabet.index(character)]
        elif character in upperAlphabet:
            encMessage += newUpperAlphabet[upperAlphabet.index(character)]
        else:
            encMessage += character

    return encMessage



def decrypt(message, key):
    lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
    newLowerAlphabet = lowerAlphabet[key:] + lowerAlphabet[:key]
    upperAlphabet = lowerAlphabet.upper()
    newUpperAlphabet = newLowerAlphabet.upper()

    decMessage = ""
    for character in message:
        if character in lowerAlphabet:
            decMessage += lowerAlphabet[newLowerAlphabet.index(character)]
        elif character in upperAlphabet:
            decMessage += upperAlphabet[newUpperAlphabet.index(character)]
        else:
            decMessage += character

    return decMessage


# Collaboration Statement:
# I worked on the homework(lab) assignment alone, using only previous and current course materials.
