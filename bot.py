# This is a sample Python script.
import time
import pyautogui
import random



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.\

class phraseHolder:
    def __init__(self, word, timer=15, next=-1, repeat=-1):
        self.word = word
        self.timer = timer  # Time before next phrase
        self.next = next    # Array index of next phrase to type
        self.repeat = repeat    # Number of time this phrase is allowed/used negative numbers repeat indefinitely

random_words = []
import csv
with open('phrase_list.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row) > 3:
            random_words.append(phraseHolder(row[0], int(row[1]), int(row[2]), int(row[3])))
        elif len(row) == 3:
            random_words.append(phraseHolder(row[0], int(row[1]), int(row[2])))
        elif len(row) == 2:
            random_words.append(phraseHolder(row[0], int(row[1])))
        elif len(row) == 1:
            random_words.append(phraseHolder(row[0]))



sleep_time = 15
next_phrase = -1 # -1 means random


def typePhrase(phrase):
    if phrase.repeat != 0:
        pyautogui.typewrite(phrase.word)
        sleep_time = phrase.timer
        next_phrase = phrase.next
        time.sleep(.5) #allow a second between typing and sending to prevent spam detection.
        pyautogui.press('enter')
        phrase.repeat = phrase.repeat - 1
        if phrase.repeat < -1:
            phrase.repeat = -1
    else:
        sleep_time = 1
        next_phrase = -1


def print_hi(name):
    phrase = phraseHolder("")
    time.sleep(sleep_time)  # Waits 15 seconds before starting
    while 1 == 1:
        if next_phrase == -1:
            phrase = random.choice(random_words)
        else:
            try:
                phrase = random_words[next_phrase]
            except:
                phrase = random.choice(random_words)

        typePhrase(phrase)
        time.sleep(sleep_time + random.randint(0, 9))


#

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/