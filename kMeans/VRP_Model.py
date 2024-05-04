import random
import math


class Model:

    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        depot = Node(0, -2, 0, 0) 
        arrive = Node(0, 2, 0, 0) 
        self.allNodes.append(depot)
        self.capacity = 18
        totalCustomers = 17
        all_x = [3, -1, 1, -6, -4, -4, 1, -6, 3, -4, -3, -1, 7, 5, 6, 2, -5]
        all_y = [-2, -2, 6, 5, 6.5, -4, -4, -3, 2, 2, -1, 4, 2, -7, 6, -7, -6]
        demand = [56, 70, 95, 28, 23, 40, 42, 61, 15,  42, 72, 63, 24, 64, 52, 24, 63]
        
        

        for i in range (0, totalCustomers):
            x = all_x[i]
            y = all_y[i]
            profit = demand[i]
            cust = Node(i + 1, x, y, profit)
            self.allNodes.append(cust)
            self.customers.append(cust)
        self.allNodes.append(arrive)
        rows = len(self.allNodes)   # 300
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]  # Here we initialize the matrix

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist    # Here we fill the matrix

class Node:
    def __init__(self, idd, xx, yy, prof):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.profit = prof
        self.isRouted = False

class Route:
    def __init__(self, dp,ar, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp) # Here we append the depot (as a starting point)
        self.sequenceOfNodes.append(ar) # Here we append it again as the last point of the route (because routes are closed)
        self.cost = 0
        self.capacity = cap
        self.load = 0
        self.prof = 0