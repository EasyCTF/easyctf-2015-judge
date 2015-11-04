import os
import random

from generators import common


def pig_latin(string):
    words = string.split(" ")
    new_words = []
    for word in words:
        if word[0] in "aeiouAEIOU":
            new_words.append(word + "yay")
        else:
            if word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                beginning = word[1:]
                if len(beginning) > 1:
                    beginning = beginning[0].upper() + beginning[1:]
                else:
                    beginning = beginning.upper()
                new_words.append(beginning + word[0].lower() + "ay")
            else:
                new_words.append(word[1:] + word[0] + "ay")
    return " ".join(new_words)


def generate(full_path):
    try:
        chosen = random.sample(set(common.sentences), 10)
        for i in range(10):
            sentence = chosen[i]
            output = pig_latin(sentence)
            f = open(full_path + os.sep + "test" + str(i) + ".in", "w")
            f.write("%s\n" % output)
            f.close()

            f = open(full_path + os.sep + "test" + str(i) + ".out", "w")
            f.write("%s\n" % sentence)
            f.close()
        return 1
    except:
        return 0
