Max=5
Tos=-1
def push(list,item):
    global Max
    global Tos
    if Tos==Max-1:
        print("stack is full")
    else:
        Tos=Tos+1
        list.append(item)
        print(item,"pushed")
def pop_element(list):
    global Tos
    if Tos==-1:
        print("stack is empty.........")
    else:
        Tos=Tos-1
        print("the element popped is :",list.pop())
list=[]
while True:
    print("1.push")
    print("2.pop")
    print("3.isEmpty")
    print("4.size")
    print("5.top of stack element")
    print("6.for exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        while True:
            print("enter element,0 to quit")
            item=int(input())
            if item == 0:
                break
            push(list,item)
push(list,10)
push(list,20)
push(list,30)
push(list,40)
push(list,50)
push(list,60)
pop_element(list)
pop_element(list)
pop_element(list)
pop_element(list)
pop_element(list)



