"""#program to reverse a given number
class reversenum:
    def __init__(self):
        self.reverse=0
    def accept(self):
            self.n=int(input("enter the number"))
    def process(self):
        while self.n>0:
            r=self.n%10
            self.reverse=self.reverse*10+r
            self.n=self.n//10
    def output(self):
        print("the reverse number :",self.reverse)
d=reversenum()
d.accept()
d.process()
d.output()

#program to check the given number is palindrome or not
class palindromenum:
    def __init__(self):
        self.reverse=0
    def accept(self):
        self.n=int(input("enter a number :"))
        self.num=self.n
    def process(self):
        while(self.n>0):
            r=self.n%10
            self.reverse=self.reverse*10+r
            self.n=self.n//10
    def check(self):
        if(self.reverse==self.num):
            print("palindrome")
        else:
            print("not palindrome")
d=palindromenum()
d.accept()
d.process()
d.check()

#program to print sum of square of given number
class square:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter a number :"))
    def process(self):
        while(self.n>0):
            r=self.n%10
            self.sum=self.sum+r**2
            self.n=self.n//10
    def output(self):
        print(self.sum)
d=square()
d.accept()
d.process()
d.output()

#program to find the given number is amstrong or not
#program to find number of digits in given number
class demo:
    def __init__(self):
        self.count=0
    def accept(self):
            self.n=int(input("enter a number :"))
    def process(self):
        while(self.n>0):
            self.count=self.count+1
            self.n=self.n//10
        print("no. of digits:",self.count)
d=demo()
d.accept()
d.process()

#program to evaluate b to power p(b**p)
class power:
    def __init__(self):
        self.res=1
        self.c=1
    def accept(self):
        self.b=int(input("enter a number :"))
        self.p=int(input("enter a number :"))
    def process(self):
        while(self.c<=self.p):
            self.res=self.res*self.b
            self.c=self.c+1
        print("power is:",self.res)
d=power()            
d.accept()
d.process()
"""
#amstrong
class amstrong:
     def __init__(self):
        self.count=0
        self.sum=0
     def accept(self):
         self.n=int(input("enter a number :"))
     def finddigitcount(self):
         num=self.n
         while(num>0):
            self.count=self.count+1
            num=num//10
         print("power:",self.count)
         return self.count
     def power(self,b,p):
         result=1
         c=1
         while c<=p:
             result=result*b
             c=c+1
         return result
     def process(self):
         num=self.n
         p=self.finddigitcount()
         while num>0:
              r=num%10
              self.sum=self.sum+self.power(r,p)
              num=num//10
         if (self.n==self.sum):
            print("amstrong")
         else:
            print("not amstrong")
d=amstrong()
d.accept()
d.process()
                        
                            
         
            
    
        

            
