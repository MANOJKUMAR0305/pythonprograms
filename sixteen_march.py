16/3/2023
"""u#program to display mathematical table
class tabletest():
    def __init__(self):
        pass
    def input(self):
        self.n=int(input("enter a number:"))
    def mul(self):
        for i in range(1,11):
            print(self.n,"*",i,"=",self.n*i)
obj=tabletest()
obj.input()
obj.mul()

#program to check given no. is prime or not
class prime_number():
    def __init__(self):
        self.c=2
        self.r=1
    def input(self):
        self.n=int(input("enter a value:"))
    def prime(self):
        while(self.c<=self.n/2 and self.r!=0):
            self.r=self.n%self.c
            self.c+=1
        if(self.r!=0):
            print("prime no.")
        else:
            print("not prime")
obj=prime_number()
obj.input()
obj.prime()                    
"""

#program to find gcd of 2 no.s
class GCD():
    def __init__(self):
        pass
    def input(self):
        self.a=int(input("enter a value:"))
        self.b=int(input("enter b value:"))
    def process(self):
        while (self.a!=self.b):
            if (self.a>self.b):
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        print(self.a)
obj=GCD()
obj.input()
obj.process()

        
