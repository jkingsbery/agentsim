from numpy import matrix
import random

class Agent:
    def __init__(self):
        self.quantity=random.randrange(10)
        self.cash=random.randrange(100)
        self.reservation_price=8 
        self.market_rate=10
        self.cost_to_create=5
        self.value_to_consume=8

    def iterate(self):
        pass


class BuyingAgent:
    def __init__(self):
        self.quantity=10
        self.most_wanted=100
        self.reserve_price=max(random.normalvariate(8,2),0)
        print "Agent reserve price " + str(self.reserve_price)
        self.price=6

    def update(self):
        if self.price<self.reserve_price and self.quantity<self.most_wanted:
            self.quantity+=1
            self.price+=1
        
class SellingAgent:
    def __init__(self):
        self.b=0
        self.m=1
        self.quantity=4
        self.price=self.marginalCost(self.quantity)
        self.last_revenue=0

    def fillOrders(self,buyingAgents):
        buying=filter(lambda x:x.price>=self.price,buyingAgents)
        sold=sum(map(lambda x:x.quantity,buying))
        print buying
        self.last_revenue=sum(map(lambda x:x.price*x.quantity,buying))

        if self.quantity>sold:
            self.quantity-=0.1
        elif self.quantity<sold:
            self.quantity+=0.1
        self.price=self.marginalCost(self.quantity)

    def __str__(self):
        return "<Price="+str(self.price)+",Quantity="+str(self.quantity)+",Revenue="+str(self.last_revenue)+">"


    def marginalCost(self,quantity):
        return self.m*quantity+self.b


if __name__=="__main__":
    random.seed(13)
    NUM_ITERS=100
    NUM_BUYERS=2
    selling=SellingAgent()
    buyers=[]
    for i in range(NUM_BUYERS):
        buyers.append(BuyingAgent())

    for iter in range(NUM_ITERS):
        selling.fillOrders(buyers)
        for x in buyers:
            x.update()
        print selling
