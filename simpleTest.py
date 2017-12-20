import sys
import urllib
import math

def stringFunc():
    outputStr = ""
    inputStr = "Mr John Smith   "
    outputStr = inputStr.rstrip().replace(" ", "%20")
    print("outputStr: %s" % outputStr)

def fileHandle():
    #Use the file name mbox-short.txt as the input file name
    #fname = input("Enter file name: ")
    #firstFloat = input("Enter float value: ")
    floatConfidence = 0.0
    #print(floatConfidence)
    count = 0
    averageConfidence = 0.0
    try:
        fh = open("mbox-short.txt")
        #fh = open("fname")
        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:"): continue
            #print(line)
            count = count + 1
            floatConfidence = floatConfidence + float(line.lstrip("X-DSPAM-Confidence: "))
            #print("float confidence = %f" % floatConfidence)
        averageConfidence = floatConfidence/count
        print("Ave Spam confidence: %0.12f" % averageConfidence)
        print("Done")
    except:
        print("No such a file in the folder.")

def camelCase():
    s = input("Enter a Camel string: ").strip()
    count = 0
    uppers = [l for l in s if l.isupper()]
    allWords = len(uppers)
    print("1. All has %s words." % allWords)
    for letter in s:
        if letter.isupper():
            count = count +1
    print("2. All has %s words." % count)

def timeInWords():
    h = int(input("Enter the hour:").strip())
    m = int(input("Enter the minute:").strip())
    minWordsDict = {0: "",
                    1: "one minute past ",
                    2: "two minutes past ",
                    3: "three minutes past ",
                    4: "four minutes past ",
                    5: "five minutes past ",
                    6: "six minutes past ",
                    7: "seven minutes past ",
                    8: "eight minutes past ",
                    9: "nine minutes past ",
                    10: "ten minutes past ",
                    11: "eleven minutes past ",
                    12: "twelve minutes past ",
                    13: "three minutes past ",
                    14: "four minutes past ",
                    15: "quater past",
                    16: "sixteen minutes past ",
                    17: "seventeen minutes past ",
                    18: "eighteen minutes past ",
                    19: "nineteen minutes past ",
                    21: "twentyone minutes past ",
                    22: "twentytwo minutes past ",
                    23: "twentythree minutes past ",
                    24: "twentyfour minutes past ",
                    25: "twentyfive minutes past ",
                    26: "twentysix minutes past ",
                    27: "twentyseven minutes past ",
                    28: "twentyeight minutes past ",
                    29: "twentynine minutes past ",
                    30: "half past ",
                    31: "thirtyone minutes past ",
                    32: "thirtytwo minutes past ",
                    33: "thirtythree minutes past ",
                    34: "thirtyfour minutes past ",
                    35: "thirtyfive minutes past ",
                    36: "thirtysix minutes past ",
                    37: "thirtyseven minutes past ",
                    38: "thirtyeight minutes past ",
                    39: "thirtynine minutes past ",
                    40: "twenty minutes to ",
                    41: "nineteen minutes to ",
                    42: "eighteen minutes to ",
                    43: "seventeen minutes to ",
                    44: "sixteen minutes to ",
                    45: "one quarter to ",
                    46: "forteen minutes to ",
                    47: "thirteen minutes to ",
                    48: "twelve minutes to ",
                    49: "eleven minutes to ",
                    50: "ten minutes to ",
                    51: "nine minutes to ",
                    52: "eight minutes to ",
                    53: "seven minutes to ",
                    54: "six minutes to ",
                    55: "five minutes to ",
                    56: "four minutes to ",
                    57: "three minutes to ",
                    58: "two minutes to ",
                    59: "one minute to "
    }
    hourWordsDict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "one"}
    if (m >= 60 and m < 0) or (h>=12 and h<1):
        print("Hour(1~12) or Minutes(0~60) are out of range.")
    elif 0<m<30:
        hrInWwords = hourWordsDict.get(h)
    elif m>=30:
        hrInWwords = hourWordsDict.get(h+1)
    elif m == 0:
        hrInWwords = hourWordsDict.get(h) + " o'clock"

    print(minWordsDict.get(m) + hrInWwords)

def totalNScore():
    # WRITE YOUR CODE HERE
    n = 8
    blocks = [5, -2, 4, 'Z', 'X', '9', '+', '+']
    newBlocks = [0]*n
    currentScore = 0
    lastScore = 0
    totalScore = 0
    last2Score = 0
    last3Score = 0

    for x in range(n):
        if blocks[x] == 'X':
            newBlocks[x] = newBlocks[x-1]*2
            newBlocks.append(blocks[x])
            newBlocks.append(currentScore)

        elif blocks[x] == '+':
            last3Score = last2Score
            last2Score = lastScore
            lastScore = currentScore
            currentScore = lastScore + last2Score
            newBlocks.append(currentScore)

        elif blocks[x] == 'Z':
            # currentScore = lastScore
            # lastScore = last2Score
            # last2Score = last3Score
            newBlocks.remove(currentScore)

        else:
            newBlocks.append(blocks[x])

        totalScore = totalScore + int(currentScore)

    print(totalScore)

def totalScore( ):
    item = []
    itemAssociation = [[1, 2], [3, 4], [4, 5]]

    for i in range(len(itemAssociation)-1):
        for i2 in range(i+1, len(itemAssociation)):
            if itemAssociation[i][0] == itemAssociation[i2][0]:
                item = itemAssociation[i]
                item.append(itemAssociation[i2][1])
            elif itemAssociation[i][1] == itemAssociation[i2][0]:
                item = itemAssociation[i]
                item.append(itemAssociation[i2][1])
            elif itemAssociation[i][0] == itemAssociation[i2][1]:
                item = itemAssociation[i]
                item.append(itemAssociation[i2][0])
            elif itemAssociation[i][1] == itemAssociation[i2][1]:
                item = itemAssociation[i]
                item.append(itemAssociation[i2][0])
    print(item)

def totalOldScore( ):
    # WRITE YOUR CODE HERE
    n = 8
    blocks = [5, -2, 4, 'Z', 'X', '9', '+', '+']
    currentScore = 0
    lastScore = 0
    totalScore = 0
    last2Score = 0
    last3Score = 0

    for x in range(n):
        if blocks[x] == 'X':
            last3Score = last2Score
            last2Score = lastScore
            lastScore = currentScore
            currentScore = 2 * lastScore
            totalScore = totalScore + int(currentScore)

        elif blocks[x] == '+':
            last3Score = last2Score
            last2Score = lastScore
            lastScore = currentScore
            currentScore = lastScore + last2Score
            totalScore = totalScore + int(currentScore)

        elif blocks[x] == 'Z':
            totalScore = totalScore - int(currentScore)
            currentScore = lastScore
            lastScore = last2Score
            last2Score = last3Score

        else:
            last3Score = last2Score
            last2Score = lastScore
            lastScore = currentScore
            currentScore = int(blocks[x])
            totalScore = totalScore + int(currentScore)

    print(totalScore)

def equalizeArray():
    #i = 8
    #arrayA =[96, 96, 45, 52, 73, 44,  51, 96]
    i = 48
    arrayA = [79, 24, 24, 24, 24, 24, 79, 79, 79, 79, 79, 24, 79, 24, 24, 79, 79, 79, 79, 24, 24, 24, 79, 24, 24, 24,
              24, 79, 79, 79, 79, 24, 24, 79, 24, 79, 79, 79, 79, 24, 79, 24, 79, 24, 79, 79, 79, 79]
    #i = int(input().strip())
    #arrayA = list(input().strip())
    for x in arrayA:
        if ' ' in arrayA:
            arrayA.remove(' ')

    max = 1
    for index in range(i-1):
        cnt = 1
        for j in range(index+1, i):
            if arrayA[index] == arrayA[j]:
                cnt = cnt + 1
            if cnt > max:
                max = cnt
    print(i-max)

def Modified_Kaprekar_Numbers():
    #p = 1; q = 100;
    kaprekar_list = []
    #for num in range(p, q+1):
    l_num = [1, 9, 45, 49, 55, 99]
    for num in l_num:
        num_len = len(str(num))

        square_num = num * num

        total_n = 0;
        for i in range(6):
            list_n = square_num % pow(10, num_len)
            square_num = int(square_num/pow(10, num_len))
            total_n = total_n + list_n
        if num == total_n:
            kaprekar_list.append(num)
    if len(kaprekar_list) > 0:
        for i in kaprekar_list:
            print(i, end=' ')
    else:
        print("INVALID RANGE")

def cavity_map():
    # n = int(input().strip())
    # t = []
    # #read the matrix input into a 2-dimession array t[][]
    # for i in range(n):
    #     grid_t = str(input().strip())
    #     t.append(grid_t)
    # print(t)
    n = 4
    t = ['1734', '5989', '2698', '6958']

    for i in range(n):
        grid = []
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n-1:
                grid.append(t[i][j])
            elif (t[i][j]>t[i][j - 1]) and (t[i][j]>t[i][j + 1]) and (t[i][j]>t[i-1][j]) and (t[i][j]>t[i+1][j]):
                grid.append('X')
            else:
                grid.append(t[i][j])
            print(grid[j], end='')
        print(end='\n')

class nodeLinkedStructured:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

head = nodeLinkedStructured("myteststring:")
node1 = nodeLinkedStructured(1)
node2 = nodeLinkedStructured(2)
node3 = nodeLinkedStructured(3)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = head

def linked_structure(node):
    count = 0
    while node and count <15:
        print(node, end=" ")
        node = node.next
        count = count + 1

def recursiveDo_n(c, n):
    if n <= 0:
        return 1
    print(' '*c + '#'*n +' '*c)
    recursiveDo_n(c+1, n - 2)

def factorial(n):
    if not isinstance(n, int):
        print("The factorial input must be an integer.")
    elif (n == 0):
        return 1
    else:
        return n * factorial(n-1)

def fermat_input_prompt(a, b, n):
    c = float((pow(a, n)+pow(b, n)**(1/n)))
    if isinstance(c, int):
        return True
    else:
        return False


def testPrint(n):
    for i in range(n):
        print(" " * (n - 1 - i) + "#" * (i + 1))

def readFromConsole(inputLine):
    print(inputLine)

def playlist(songs, k, q):
    minNum = 0
    totalLengthOfSong = songs.__len__()

    for i in range((songs.index(q) + 1), totalLengthOfSong):
        if songs[i] == q:
            print("secondNum = %d" % i)

    indexOfQ = songs.index(q)
    print("indexOfQ = %s" % indexOfQ)

    minNum = min(abs(indexOfQ - k), totalLengthOfSong - abs(indexOfQ - k))

    return minNum

if __name__ == "__main__":
    #print(myNode)
    #linked_structure(head)
    #songs = ['I', 'we', 'he', 'you', 'he']
    #k = 1
    #q = 'he'
    #print(playlist(songs, k, q))

    #chapter 6 String
    #stringFunc()

    #chapter 7 file handler
    #fileHandle()

    #camelCase()
    #timeInWords()
    #equalizeArray()
    #cavity_map()
    #recursiveDo_n(0, 5)
    #print(factorial(3))

    print("Fermat input is: ", fermat_input_prompt(1, 2, 3))

    #Amazon Test
    #totalScore()

    #Modified_Kaprekar_Numbers()

    #execute only if run as a script
    #testPrint(6)
    #print("Please write your input values here:")
    #inputLine = input()
    #readFromConsole(inputLine)

    