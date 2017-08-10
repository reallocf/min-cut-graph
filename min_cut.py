#!/usr/bin/env python
from sys import argv
from copy import deepcopy
import random

class Graph:
    def __init__(self, parsedInputList):
        self.nodeMap = self.node_map_maker(parsedInputList)

    def node_map_maker(self, parsedInputList):
        nodeMap = {}
        for node in parsedInputList:
            nodeMap[node[0]] = node[1:]
        return nodeMap

    def __str__(self):
        ret = ""
        nodeCount = 0
        edgeCount = 0
        for node in sorted(self.nodeMap.keys()):
            nodeCount += 1
            edgeCount += len(self.nodeMap[node])
            ret += str(node) + ": " + str(self.nodeMap[node]) + "\n"
        ret += "node count: " + str(nodeCount) + "\nedge count: " + str(edgeCount)
        return ret

    def pick_node(self):
        return random.choice(list(self.nodeMap.keys()))

    def pick_connected(self, node):
        return random.choice(self.nodeMap[node])

    def contract(self):
        node1 = self.pick_node()
        node2 = self.pick_connected(node1)
        self.nodeMap[node1] += self.nodeMap[node2]
        for edge in self.nodeMap[node2]:
            self.nodeMap[edge].remove(node2)
            self.nodeMap[edge].append(node1)
        while node1 in self.nodeMap[node1]:
            self.nodeMap[node1].remove(node1)
        del self.nodeMap[node2]

def parse(inputList):
    with open(inputList, "r") as f:
        return [list(map(int, elem.split('\t')[:-1])) for elem in f.read().split('\n')[:-1]]

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage ./min_cut.py adjacency_list.txt")
        exit()
    graph = Graph(parse(argv[1]))
    print(graph)
    minCount = None
    for i in range(100):
        tempGraph = deepcopy(graph)
        while(len(tempGraph.nodeMap) > 2):
            tempGraph.contract()
        tempCount = len(tempGraph.nodeMap[list(tempGraph.nodeMap.keys())[0]])
        print("Temp count "+ str(i) + " is: " + str(tempCount))
        if minCount == None or tempCount < minCount:
            minCount = tempCount
    print("Min count is: " + str(minCount))
