from matplotlib.cbook import print_cycles
from VRP_Model import *
from SolutionDrawer import *

class Solution:
    def __init__(self):
        self.cost = 0.0
        self.prof = 0.0
        self.routes = []



class CustomerInsertionAllPositions(object):
    def __init__(self):
        self.customer = None
        self.route = None
        self.insertionPosition = None
        self.cost = 10 ** 12
        self.prof = 0
        self.knapsack = 0

class Solver:
    def __init__(self, m):
        self.allNodes = m.allNodes
        self.customers = m.customers
        self.depot = m.allNodes[0]
        self.arrive = m.allNodes[-1]
        self.distanceMatrix = m.matrix
        self.capacity = m.capacity
        self.sol = None
        self.bestSolution = None
        self.searchTrajectory = []

    def solve(self):
        self.SetRoutedFlagToFalseForAllCustomers()
        self.MinimumInsertions()
        self.ReportSolution(self.sol)
        return self.sol

    def SetRoutedFlagToFalseForAllCustomers(self):
        for i in range(0, len(self.customers)):
            self.customers[i].isRouted = False

    def Always_keep_an_empty_route(self):
        if len(self.sol.routes) != 3:
            rt = Route(self.depot,self.arrive, self.capacity)
            self.sol.routes.append(rt)

    # This method conducts the minimum insertion method along with a knapsack comparison in its decision-making process of picking customers          
    def IdentifyMinimumCostInsertion(self, best_insertion):
        for i in range(0, len(self.customers)):
            candidateCust: Node = self.customers[i]
            if candidateCust.isRouted is False:
                for rt in self.sol.routes:
                    if rt.cost <= rt.capacity: 
                        for j in range(0, len(rt.sequenceOfNodes) - 1):
                            A = rt.sequenceOfNodes[j]
                            B = rt.sequenceOfNodes[j + 1]
                            costAdded = self.distanceMatrix[A.ID][candidateCust.ID] + self.distanceMatrix[candidateCust.ID][B.ID]
                            costRemoved = self.distanceMatrix[A.ID][B.ID]
                            trialCost = costAdded - costRemoved
                            trialprof = candidateCust.profit
                            knapsack = (-(10**12)*trialprof)    # Here we multiply with a very negative large number so we 
                            if rt.cost + trialCost > rt.capacity:           # turn this maximazitation problem to a minimization problem
                                continue
                            if knapsack < best_insertion.knapsack:          # Here we pick the customer(Node) with the best profit per
                                best_insertion.customer = candidateCust     # cost ratio of the iteration
                                best_insertion.route = rt
                                best_insertion.cost = trialCost
                                best_insertion.insertionPosition = j
                                best_insertion.profit = trialprof
                                best_insertion.knapsack = knapsack
                            else:
                                continue
                    else:
                        continue
                
    def MinimumInsertions(self):
        self.sol = Solution()
        while len(self.sol.routes) <= 3:           # Here we allow the creation of five routes as we have five trucks                  
            best_insertion = CustomerInsertionAllPositions()
            self.Always_keep_an_empty_route()
            self.IdentifyMinimumCostInsertion(best_insertion)

            if best_insertion.customer is not None:
                self.ApplyCustomerInsertionAllPositions(best_insertion)
            else:
                break

    def ReportSolution(self, sol): 
        # Here we print every route, its nodes along with its cost and profit, of the initial without any use of operators
        for i in range(0, len(sol.routes)):
            rt = sol.routes[i]
            for j in range (0, len(rt.sequenceOfNodes)):
                print(rt.sequenceOfNodes[j].ID, end=' ')
            print("Cost:", round(rt.cost,2), "Profit:", rt.prof)
        SolDrawer.draw('MinIns', self.sol, self.allNodes)
        print("Total Cost:", self.sol.cost, "Total Profit:", self.sol.prof)


    def ApplyCustomerInsertionAllPositions(self, insertion):
        insCustomer = insertion.customer
        rt = insertion.route
        insIndex = insertion.insertionPosition
        rt.sequenceOfNodes.insert(insIndex + 1, insCustomer)
        rt.cost += insertion.cost
        self.sol.cost += insertion.cost
        rt.prof += insCustomer.profit
        self.sol.prof += insCustomer.profit
        insCustomer.isRouted = True


