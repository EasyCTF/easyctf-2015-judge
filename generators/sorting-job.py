import os
import random


def generate(full_path):
    try:
        numList = list()
        for i in range(10):
            for a in range(10):
                num = random.randint(0, 100)
                numList.append(num)
            f = open(full_path + os.sep + "test" + str(i) + ".in", "w")
            f.write("%s\n" % ",".join([str(j) for j in numList]))
            f.close()
            b = sorted(numList, reverse=True)
            output = ",".join([str(j) for j in b]) + "\n"
            f = open(full_path + os.sep + "test" + str(i) + ".out", "w")
            f.write("%s" % output)
            f.close()
            numList = []
        return 1
    except:
        return 0
