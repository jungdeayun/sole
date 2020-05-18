def add(a, b):
    return a+b

class Woman:
    def __init__(self, weight, height, iq):
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat(self):
        print("-------------")
        print("eat method")
        print("weight : ", self.weight + 10)
        print("height : ", self.height)
        print("iq : ", self.iq)

    def study(self):
        print("-------------")
        print("study method")
        print("weight : ", self.weight - 10)
        print("height : ", self.height)
        print("iq : ", self.iq + 10)

    def sleep(self):
        print("-------------")
        print("sleep method")
        print("weight : ", self.weight)
        print("height : ", self.height + 10)
        print("iq : ", self.iq + 5)