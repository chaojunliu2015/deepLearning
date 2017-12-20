import sys
import random
import math
import time
#import numpy.py

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def __str__(self):
        return str(self.it + str([x.id for x in self.connectedTo]))

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo(nbr)

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

band_dict = {'LTE': 3.0,
             'WCDMA': 1.9,
             '1xEVDO': 2.1,
             'GSM' : 0.9
             }
band_list= ['LTE', 'WCDMA', 'EVDO', 'GSM']
band_tupple = []
class communicationTest(object):
    """from the band(LTE, WCDMA, C2K, 1xEVDO, GSM) to find out the uplink and downlink freqrange"""
    def __init__(self, band, freq_range):
        self.band = band
        self.freq_range = freq_range

class Node(object):
    """Linked list."""
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return  str(self.cargo)

    #def print_point(self):
    #    print(self.x, self.y)

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

node4.cargo = node1

def printList(Node):
    while Node:
        print(Node.cargo)
        Node = Node.next

"""
The Ackermann function, A(m, n), is defined:
A(m, n) =     n+1	if  m = 0
        A(m−1, 1)	if  m > 0  and  n = 0
A(m−1, A(m, n−1))	if  m > 0  and  n > 0.

Use your function to evaluate ack(3, 4), which should be 125.
What happens for larger values of m and n? 
"""
def ack(m, n):
    try:
        if (m <= 0 and n <= 0):
            print("ilegal numbers reached")
            return None
        elif m==0:
            return n+1
        elif(m >0 and n==0):
            return ack(m-1, 1)
        elif(m>0 and n>0):
            return ack(m-1, ack(m, n-1))
    except:
        print("m or n is too large.")

def middle(word):
    return word[1:-1]
def is_palindrome(word):
    if word == '':
        print("The word '%s'is a null string." % word)
    else:
        for i in range(int(len(word)/2)):
            if word[i]!= word[-1-i]:
                print("The word '%s' is NOT a palindrome." % word)
                return False
            else:
                continue
        print("The word '%s'is a palindrome." % word)
        return True

def fibonacci(n):
    if (n < 0):
        print("Negtive number has no fibonacci result!")
    elif(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

known={0:0, 1:1}
def fibonacci_hashble(n):
    if n< 0:
        print("Negitave number has no fibonacci result!")
    elif(n in known):
        return known[n]
    else:
        result = fibonacci_hashble(n-1)+fibonacci_hashble(n-2)
        known[n] = result
    return result

def test_square_root(a, x):
    while True:
        y = (x + (a/x)) / 2
        if (y - x < 0.000001):
            break
    x = y
    print(a, math.sqrt(a), x, abs(x-math.sqrt(a)))

def historical(input_string):
    d = dict()
    for c in input_string:
        c_count = d.get(c, 0)
        c_count += 1
        d[c] = c_count

        # if c in d:
        #     d[c] += 1
        # else:
        #     d[c] = 1
    print(d)
    #print(reverse_lookup(d, 5))
    #print_historical(d)
    invert_dict(d)
def print_historical(h):
    n_list = []
    n_list = list(h.keys())
    n_list.sort()

    for c in n_list:
        print(c, h.get(c))
def reverse_lookup(d, v):
    k_list = []
    for k in d:
        if d[k] == v:
            k_list.append(k)
    return k_list
    #raise ValueError('value %s not appear in the dictionary.' %v)
    #raise Warning('value %s has NONE key in the dictionary.' %v)
def invert_dict(d):
    invert = dict()
    for k in d:
        val = d[k]
        if val not in invert:
            invert[val] = [k]
        else:
            invert[val].append(k)
        #invert.setdefault(d[k], [k])
    print(invert)

def sumall(*arg):
    res = 0
    for i in arg:
        res = res + i
    return res
def sort_by_length(words):
    t = []
    for w in words:
        t.append((len(w), w))
    t.sort(reverse= True)
    res = []
    for l, wd in t:
        res.append(wd)
    return res

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        position = i
        current_value = a_list[i]
        while position > 0 and a_list[position] < a_list[position - 1]:
            a_list[position] = a_list[position - 1]
            position = position -1
        a_list[position] = current_value

def ReutersTest(nums, maxs):
    answer = []

    for i in range(maxs.__len__()):
        count = 0
        for j in range(nums.__len__()):
            if (nums[j] <= maxs[i]):
                count += 1
        answer.append(count)
    return answer

def Reuters_customized_sord(a):
    answer = 1
    #if a = [13, 10, 21, 20], answer = 1. Because result = [20, 10, 21, 13], minimum 1 time to move all even nums before odd nums

    return answer


def Reuters_braces(values):
    result = "YES"
    # if values = {}[](), result = "YES"; if values = {[}], result = "NO"

    return result

if __name__ == "__main__":

    print("Program started here.")
    # f_num = input("How many Fibonacci number needed?")
    # n = int(f_num)
    # fibonacci_list=[]
    # fibonacci(0)
    # fibonacci(1)
    # for i in range(int(n)):
    #     fibonacci_list.append(fibonacci(i))
    # print("%d Fibonacci list =" % n, fibonacci_list )
    #hashble_r=fibonacci_hashble(50)
    #print("Fibonacci hashble result = ", hashble_r)

    #Ackermann = ack(4, 5)
    #print(Ackermann)

    #print(is_palindrome('abvdaavba'))
    #test_square_root(4, 2)
    #historical('Are you my friend?')
    # t = (1, 2, 3, 4, 5)
    # print(sumall(*t))

    #res = sort_by_length(['a', 'ab', 'cd', 'efg', 'heard'])
    #print(res)

    #printList(node1)

    # alist = [54,26,93,17,77,31,44,55,20]
    # insertion_sort(alist)
    # print(alist)
    print(ReutersTest([2, 3, 4, 5, 9], [3, 7, 4, 1]))

    # g = Graph()
    # for i in range(6):
    #     g.addVertex(i)
    # g.addEdge(0, 1, 5)
    # g.addEdge(0, 5, 2)
    # g.addEdge(1, 2, 4)
    # g.addEdge(2, 3, 9)
    # g.addEdge(3, 4, 7)
    # g.addEdge(3, 5, 3)
    # g.addEdge(4, 0, 1)
    # g.addEdge(5, 4, 8)
    # g.addEdge(5, 2, 1)
    # for v in g:
    #     for w in v.getConnections():
    #         print("(%s, %s" %(v.getId, w.getId))
