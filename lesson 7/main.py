

class Queue():
    def __init__(self):
        self.queue=[]
        self.size=len(self.queue)
    
    def Enqueue(self,value):
        self.queue.append(value)

    def Dequeue(self):
        if len(self.queue)>0:
            self.queue.pop(0)
        else:
            print('The queue is empty')

    def front(self):
        if len(self.queue)>0:
            print(self.queue[0])
        else:
            print('The queue is empty')

    def rear(self):
        if len(self.queue)>0:
            print(self.queue[self.size-1])
        else:
            print('The queue is empty')            

    def IsEmpty(self):
        if len(self.queue)==0:
            print('The queue is empty')
        else:
            print('The queue is not empty')

s=Queue()

s.Enqueue(5)
print(s.queue)
s.Enqueue(8)
print(s.queue)
s.Enqueue(1)
print(s.queue)

s.Dequeue()
print(s.queue)

s.front()
s.rear()

s.Dequeue()
s.Dequeue()
print(s.queue)

s.IsEmpty()