#!/usr/bin/env python
#
# Description:
#  Says a number outloud and takes the users answer. When pressing a key, displays the number and counter of total and wrong answers.
#
# Dependencies (pip modules):
#   gTTS playsound
# For Linux additionally: vext.gi
#
# Runs at least on Python >= 3.9 on at least Windows and Linux.
# 
# Usage:
#   ./lang_num_exercise.py <lower limit> <upper limit> <language-code>
# Example:
#  ./lang_num_exercise.py 100 1000 es 
# Will choose numbers at random between 100 and 1000 and say them in spanish.
#
import sys
import os
import gtts
from playsound import playsound
from random import randint


def action():
    if 'q' in input("Press 'q' to exit. Press enter to continue.\n"):
        os.remove(fileName)
        sys.exit()


def LangNumExercise():
    _ = os.system(CLS_CMD)
    print("Start of language number exercise.")
    action()
    total_answers = 0
    wrong_answers = 0
    while True:
        num = randint(num_range[0], num_range[1])
        tts = gtts.gTTS(str(num), lang=language)
        tts.save(fileName)
        playsound(fileName)
        user_input = int(input('\nInput the number: \n'))
        if user_input != num:
          wrong_answers += 1
        total_answers += 1
        _ = os.system(CLS_CMD)
        print("\nThe number is: %s.\nYour answer was: %s.\n" % (str(num),str(user_input)))
        print("\n\nTotal answers: %s\n" % str(total_answers))
        print("Wrong answers: %s\n" % str(wrong_answers))
        action()


if __name__ == "__main__":
    fileName = "LangNum.mp3"
    if os.name == "posix":
        CLS_CMD = "clear"
    elif os.name == "nt":
        CLS_CMD = "cls"
    else:
        print("OS not supported")
        sys.exit(1)
    if len(sys.argv) < 4:
        num_range = [0, 10000]
        language = "ru"
    else:
        num_range = [int(sys.argv[1]), int(sys.argv[2])]
        language = sys.argv[3]
    LangNumExercise()
